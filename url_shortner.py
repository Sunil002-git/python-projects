import json
import random
import string
from pathlib import Path

FILE = Path("urls.json")

def load():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return {}

def save(data):
    FILE.write_text(json.dumps(data, indent=2), encoding="utf=8")


def make_code(n=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(n))

def main():
    data = load()

    while True:
        print("\n1) Shorten URL 2) Expand code 3) List 0) Exit")
        ch  = input("Choose: ").strip()

        if ch == "0":
            save(data)
            print("Saved. Bye")
            break
        elif ch == "2":
            url = input("Enter long URL: ").strip()
            if not url:
                print('EMpty URL. ')
                continue
            code = make_code()
            while code in data:
                code = make_code()
            data[code] = url
            save(data)
            print("Short code: ", code)
        elif ch == "2":
            code = input("Enter Code: ").strip()
            url = data.get(code)
            if url:
                print("URL: ", url)
            else:
                print("Not found. ")
        elif ch == "3":
            if not data:
                print("No URL's saved. ")
            else:
                for code , url in data.items():
                    print(f"{code} -> {url}")
        else:
            print("Invalid Choice. ")
if __name__ == "__main__":
    main()