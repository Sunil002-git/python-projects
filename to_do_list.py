from pathlib import Path
FILE = Path("todos.txt")

def load_todos():
    if not FILE.exists():
        return[]
    return [line.strip() for line in FILE.read_text(encoding='utf-8').splitlines() if line.strip()]

def save_todos(todos):
    FILE.write_text("\n".join(todos) + ("\n" if todos else ""), encoding="utf-8")

def main():
    todos = load_todos()

    while True:
        print("\n1) Add 2) View 3) Done(remove) 0) Exit")
        choice = input("Choose: ").strip()

        if choice == "0":
            save_todos(todos)
            print("Saved Bye!")
            break
        elif choice == "1":
            task = input("Task: ").strip()
            if task:
                todos.append(task)
                save_todos(todos)
            else :
                print("Empty task not added. ")
        elif choice == "2":
            if not todos:
                print("No tasks")
            else:
                for i, t in enumerate(todos, start=1):
                    print(f"{i}.{t}")
        elif choice == "3":
            if not todos:
                print("No tasks to remove.")
                continue
            num = input("Enter task number to mark done: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(todos):
                    done = todos.pop(idx)
                    save_todos(todos)
                    print("Done: ", done)
                else :
                    print("Invalid Number. ")
            else:
                print("Enter a valid number")
        else:
            print("Invalid Choice. ")

if __name__ == "__main__":
    main()