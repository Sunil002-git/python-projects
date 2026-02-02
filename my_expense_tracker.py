import sqlite3
from datetime import datetime
import csv
from pathlib import Path 

DB_FILE = "expenses.db"

def connect():
    return sqlite3.connect(DB_FILE)

def init_db():
    with connect() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     tdate TEXT NOT NULL,
                     ttype TEXT NOT NULL CHECK(ttype IN('income', 'expense')),
                     category TEXT NOT NULL,
                     amount REAL NOT NULL CHECK (amount > 0),
                     note TEXT
        );
        """)
        conn.commit()
def valid_date(date_str: str)-> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def add_transaction():
     tdate = input("Date (YYYY-MM-DD) / [Today]: ").strip()
     if not tdate:
         tdate = datetime.today().strftime("%Y-%m-%d")
        #  print (tdate)
     if not valid_date(tdate):
         print("Invalid Date Format.")
         return
     ttype = input("Type (income/expense): ").strip().lower()
     if ttype not in ("income", "expense"):
         print("Type must be 'income' or 'expense'." )
         return
     category = input("Category (e.g., Food, Rent, Salary): ").strip()
     if not category:
         print("Category cannot be empty.")
         return
     
     try:
         amount = float(input("Amount: ").strip())
         if amount<=0 :
             raise ValueError
     except ValueError:
            print("Amount must be a number > 0.")
            return
     
     note = input("Note (Optional): ").strip()

     with connect() as conn:
         conn.execute("INSERT INTO transactions(tdate, ttype, category, amount, note)" \
         "VALUES (?,?, ?, ?, ?)",
           (tdate, ttype, category, amount, note or None ))
         conn.commit()
     print("Transaction Saved.")


def list_transactions(limit=50):
    with connect() as conn:
        rows = conn.execute("""SELECT id, tdate, ttype, category, amount, COALESCE(note, '') 
                            FROM transactions ORDER by 
                            tdate DESC , id DESC LIMIT ?""", (limit,)).fetchall()
    if not rows:
        print("No Transactions found.")
        return
    print("\n ID  | Date | Type    | category | Amount | Note")
    print("-" * 65)
    for r in rows:
        print(f"{r[0]:<2} | {r[1]} | {r[2]:<7} | {r[3]:<12} | {r[4]:<8.2f} | {r[5]}")
    print()


def monthly_summary():
   month = input("Enter Month (YYYY-MM) / [Current] : ").strip()
   if not month:
       month = datetime.today().strftime("%Y-%m")
   try:
        datetime.strptime(month + "-01", "%Y-%m-%d")
   except ValueError:
        print("Invalid month format.")
        return
   start = month + "-01"

   with connect() as conn:
       income = conn.execute("""
            SELECT COLESCE(SUM(amount), 0)
            FROM transactions
            WHERE ttype = 'income' AND tdate >= ? AND tdate < date(?, '+1 month')
        """, (start, start)).fetchone()[0]
       expense = conn.execute("""
            SELECT COLESCE(SUM(amount), 0)
            FROM transactions
            WHERE ttype = 'expense' AND tdate >= ? AND tdate < date(?, '+1 month')
        """, (start, start)).fetchone()[0]
   balance = income - expense
   print(f"/n Month: {month}")
   print(f"Income: {income}")
   print(f"Expense: {expense}")
   print(f"Balance: {balance:.2f}\n")
    
def category_summary():
   month = input("Enter Month (YYYY-MM) / [Current] : ").strip()
   if not month:
       month = datetime.today().strftime("%Y-%m")
   try:
        datetime.strptime(month + "-01", "%Y-%m-%d")
   except ValueError:
        print("Invalid month format.")
        return
   start = month + "-01"

   with connect() as conn:
       rows = conn.execute("""
            SELECT category, COALESCE(SUM(amount), 0) as total 
            FROM transactions 
            WHERE ttype='expense'
            AND tdate >= ? AND tdate < date(?, '+1 month')
            GROUP BY category
            ORDER BY total DESC
            """, (start, start)).fetchall()
   if not rows:
       print("No expense data for this month.")
       return
   print(f"\n Category-wise expenses for {month}")
   print("-" * 40)
   for cat, total in rows:
       print(f"{cat:<15} : {total:.2f}")
   print()

def search_transactions():
        print("\n Search filters (Press Enter to SKip)")
        start = input("Start Date (YYYY-MM-DD): ").strip()
        end = input("End Date (YYYY-MM-DD): ").strip()
        category = input("Category: ").strip()

        conditions = []
        params = []

        if start :
            if not valid_date(start):
                print("Invalid Start Date.")
                return
            conditions.append("tdate >= ?")
            params.append(start)
        if end :
            if not valid_date(end):
                print("Invalid end Date.")
                return
            conditions.append("tdate <= ?")
            params.append(end)
        if category:
            conditions.append("LOWER(category) = LOWER(?)")
            params.append(category)

        where = "WHERE " + " AND ".join(conditions) if conditions else ""

        with connect() as conn:
            rows = conn.execute(f"""
                SELECT id , tdate, ttype, category, amount, COALESCE(note, '')
                FROM transactions
                {where}
                 ORDER BY tdate DESC, id DESC
            """, params).fetchall()
        if not rows:
            print("No results.")
            return

        print("\nID | Date       | Type    | Category     | Amount   | Note")
        print("-" * 70)
        for r in rows:
            print(f"{r[0]:<2} | {r[1]} | {r[2]:<7} | {r[3]:<12} | {r[4]:<8.2f} | {r[5]}")
        print()
        
def export_csv():
    out = input("Export filename [transactions.csv]: ").strip() or "transactions.csv"
    out_path = Path(out)
    
    with connect() as conn:
        rows = conn.execute("""
            SELECT id, tdate, ttype, category, amount, COALESCE(note,'')
            FROM transactions
            ORDER BY tdate ASC, id ASC
        """).fetchall()
    if not rows:
        print("No transactions to export.")
        return
    
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "date", "type", "category", "amount", "note"])
        writer.writerows(rows)
    print(f"Exported to {out_path.resolve()}")

def delete_transaction():
    try:
        tid = int(input("Enter transaction ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    with connect() as conn:
        cur = conn.execute("DELETE FROM transactions WHERE id = ?", (tid,))
        conn.commit()

    if cur.rowcount == 0:
        print("No Transactions found with that ID.")
    else:
        print ("Deleted.")


def menu():
    print("===========Expenses Tracker==============")
    print("1) Add Transaction")
    print("2) List Transactions")
    print("3) Monthly Summary")
    print("4) Category Summary (Month)")
    print("5) Search")
    print("6) Export CSV")
    print("7) Delete Transaction")
    print("0) Exit")
    print("==========================================")

def main():
    init_db()
    while True:
        menu()
        choice = input("Choose: ").strip()
        if not choice:
            print("Please enter a choice")
            continue
        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            search_transactions()
        elif choice == "6":
            export_csv()
        elif choice == "7":
            delete_transaction()
        elif choice == "0":
            print("Bye 🙋")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()