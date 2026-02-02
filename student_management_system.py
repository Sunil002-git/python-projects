# @staticmethod
# def from_dict(d):
#     return Student(d["roll_no"], d["name"], d["marks"])
# This creates a Student object from file data
#  @staticmethod → does not depend on any object

import json
from pathlib import Path
from collections import Counter

FILE = Path("students.json")

class Student:
    def __init__(self, roll_no: int, name: str, marks: float):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    
    def to_dict(self):
        return {"roll_no": self.roll_no,
                "name": self.name,
                "marks": self.marks}
    
    @staticmethod
    def from_dict(d):
        return Student(d["roll_no"], d["name"], d["marks"])
    
def load_students():
    if not FILE.exists():
        return []
    data = json.loads(FILE.read_text(encoding="utf-8"))
    return [Student.from_dict(d) for d in data]

def save_students(students):
    data = [s.to_dict() for s in students]
    FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def main():
    students = load_students()

    while True:
        print("\n1) Add 2) List 3) Search by Roll 4) Delete 0) Exit")
        ch = input("Choose: ").strip()

        if ch == "0":
            save_students(students)
            print("Saved. Bye !")
            break
        elif ch == "1":
            try:
                roll = int(input("Roll no: ").strip())
                name = input("Name: ").strip()
                marks = float(input("Marks: ").strip())
            except ValueError:
                print("Invalid input. ")
                continue
            students.append(Student(roll, name, marks))
            save_students(students)
            print("Added")
        
        elif ch == "2":
            if not students:
                print("No students")
            else:
                for s in students:
                    if s.marks > 75:
                        print(f"{s.roll_no} | {s.name} | {s.marks}")
                print(len(students))
                total_marks = sum(s.marks for s in students)
                average_marks = total_marks/len(students)
                print(average_marks)      
        elif ch == "3":
            try:
                roll = int(input("Roll to Search: ").strip())
            except ValueError:
                print("Enter a number. ")
                continue
            print(students)
            for s in students:
                if s.roll_no == roll:
                    print(f"Found: {s.roll_no} | {s.name} | {s.marks}")
                else:
                    print("Not Found. ")
        elif ch == "4":
            try:
                roll = int(input("Roll to Delete: ").strip())
            except ValueError:
                print("Enter a number: ")
                continue
            before = len(students)
            students = [s for s in students if s.roll_no != roll]
            if len(students) < before:
                save_students(students)
                print("Deleted. ")
            else:
                print("Not Found. ")
    else:
        print("Invalid choice. ")

if __name__ == "__main__":
    main()
