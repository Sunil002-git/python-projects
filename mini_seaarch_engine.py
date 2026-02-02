from pathlib import Path
import re

DOCS_DIR = Path('docs')

def build_index():
    index = {}
    for file in DOCS_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8", errors="ignore").lower()
        words = set(re.findall(r"[a-z0-9']+", text))
        for w in words:
            index.setdefault(w, set()).add(file.name)
    return index

def main():
    if not DOCS_DIR.exists():
        print("Creates a folder named 'docs' and add some .txt files. ")
        return
    index = build_index()
    print("Index Build. Type a word to search or 'exit' ")

    while True:
        q = input("Search word: ").strip().lower()
        if q == "exit":
            break
        files = index.get(q, set())
        if files:
            print("Found in:", ", ".join(sorted(files)))
        else:
            print("No matches. ")

if __name__ == "__main__":
    main()