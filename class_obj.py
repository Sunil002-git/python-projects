# import json
# from pathlib import Path
# class Book:
#     def __init__(self, id: int, title: str, price: int):
#         self.id = id
#         self.title = title
#         self.price = price
    
#     def discount(self, percent):
#        discount_amount = self.price * percent / 100
#        self.price = self.price - discount_amount

#     def __str__(self):
#         return f"{self.id} | {self.title} | {self.price}"
#     def to_dict(self):
#         return {"id": self.id, "title" : self.title, "price" : self.price}
#     @staticmethod
#     def from_dict(d):
#         return Book(d["id"], d["title"], d["price"])
# FILE = Path("books.json")

# def load_books():
#     if not FILE.exists():
#         return []

#     data = json.loads(FILE.read_text(encoding="utf-8"))
#     return [Book.from_dict(d) for d in data]
# def save_books(books):
#     data = [b.to_dict() for b in books]
#     FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

# books = load_books()

# for b in books:
#     print(b)

# book1 = Book(1, "Nothing Lasts forever", 300)
# book2 = Book(2, "Alchemist", 200)
# book3 = Book(3, "Recursion", 180)

# books = [book1, book2, book3]

# for b in books:
#     b.discount(5)
#     print(b.price > 200)
    
#part 1
# student_dict = {
#     "roll_no" : 1,
#     "name" : "Sunil",
#     "marks" : 85.5
# }
# student_dict["name"] = "Ravi"
# print(student_dict["roll_no"])
# print(student_dict["name"])
# print(student_dict["marks"])

# class Student:
#     def __init__(self, roll_no, name, marks):
#         self.roll_no = roll_no
#         self.name = name
#         self.marks = marks
    
# student = Student(1,"Sunil", 90)
# student.name = "Suresh"
# print(student.roll_no)
# print(student.name)
# print(student.marks)

def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e)

        
divide(3, "GFG") 
divide(3,0)