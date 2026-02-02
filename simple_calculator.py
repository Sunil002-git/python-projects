def read_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Enter a valid number (e.g.. 10 or 5.5.)")
            
def main():
    while True:
        print("\n 1) Add 2) Subtract 3) Multiply 4) Divide 0) Exit")
        op = input("Choose: ").strip()

        if op == "0":
            print("Bye")
            break
        if op not in {"1", "2", "3", "4"}:
            print("Invalid Choice. ")
            continue

        a = read_number("Enter first number: ")
        b = read_number("Enter second number: ")

        if op == "1":
            print("result: ", a+b)
            break
        elif op == "2":
            print("result: ", a-b)
            break
        elif op == "3":
            print("result:", a*b)
            break
        elif op == "4":
            if b == 0:
                print("Cannot divide by zero. ")
            else:
                print("Result: ", a/b )
                break

if __name__ == "__main__":
    main()