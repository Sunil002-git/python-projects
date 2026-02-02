# Assignment in a dictionary does both create & update.
"""
Contact Book- Concepts: dictionaries, CRUD, searching, loops, file persistence (JSON)
Run: python contacts.py """

# json loads converts json string to python dictionary
# json write file converts python dictionary to json string

import json
from pathlib import Path

FILE = Path("contacts.json")

def load_contacts():
    if not FILE.exists():
        return {}
    return json.loads(FILE.read_text(encoding="utf-8"))

def save_contacts(contacts):
    FILE.write_text(json.dumps(contacts, indent=2), encoding="utf-8")

def main():
    contacts = load_contacts()

    while True:
        print("\n1) Add/Update 2) View All 3) Search 4) Delete 0) Exit")
        ch = input("Choose: ").strip()

        if ch == "0":
            save_contacts(contacts)
            print("Saved. Bye!!")
            break
        elif ch == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                contacts[name] = phone
                save_contacts(contacts)
                print("Contact Saved .")
            else:
                print("Name?Phone cannot be empty")
        elif ch == "2":
            if not contacts:
                print("No Contacts")
            else:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
        elif ch == "3":
            q = input("Enter name to Search: ").strip().lower()
            found = False
            for name , phone in contacts.items():
                if q in name.lower():
                    print(f"{name} : {phone}")
                    found = True
            if not found:
                print("No matches.")
        elif ch == "4":
            name = input("Enter name to Delete: ").strip()
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print("Deleted")
            else:
                print("Not Found .")
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()

