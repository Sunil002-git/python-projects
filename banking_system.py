import sqlite3

DB = 'bank.db'

def connect():
    return sqlite3.connect(DB)

def init_db():
    with connect() as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS accounts(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     balance REAL NOT NULL DEFAULT 0)
""")
        conn.commit()

class Bank:
    def create_account(self, name, opening=0.0):
        with connect() as conn:
            conn.execute("""
INSERT INTO accounts (name, balance) VALUES(?, ?)
""", (name, opening))
            conn.commit()
    
    def deposit(self, acc_id, amount):
        with connect() as conn:
            conn.execute("""
UPDATE accounts SET balance = balance + ? WHERE id = ?
""", (amount, acc_id))
            conn.commit()
    
    def withdraw(self, acc_id, amount):
        with connect() as conn:
            bal = conn.execute("SELECT balance FROM accounts WHERE id = ?", (acc_id,)).fetchone()
            if not bal:
                print("Account not found.")
                return
            if bal[0] < amount:
                print("Insufficient funds.")
                return
            conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, acc_id))
            conn.commit()

    def list_accounts(self):
        with connect() as conn:
            rows = conn.execute("SELECT id, name, balance FROM accounts ORDER BY id").fetchall()
            for r in rows:
                print(f"{r[0]} | {r[1]} | {r[2]: 2f}")

def main():
    init_db()
    bank = Bank()

    while True:
        print("\n 1) Create 2) Deposit 3) Withdraw 4) List 0) Exit")
        ch = input("Choose: ").strip()
        if ch == "0":
            break
        elif ch == "1":
            name = input("Name: ").strip()
            opening = float(input("Opening Balance: ").strip() or "0")
            bank.create_account(name, opening)
        elif ch == "2":
            acc = int(input("Account ID: ").strip())
            amt = float(input("AMount: ").strip())
            bank.deposit(acc, amt)
        elif ch == "3":
            acc = int(input("Account ID: ").strip())
            amt = float(input("AMount: ").strip())
            bank.withdraw(acc, amt)
        elif ch == "4":
            bank.list_accounts()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()