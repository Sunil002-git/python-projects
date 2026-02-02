from collections import Counter
import re
from pathlib import Path

def analyze(path: str):
    FILE = Path(path)
    text = FILE.read_text(encoding="utf-8", errors="ignore").lower()
    words = re.findall(r"[a-z0-9']+", text)
    counts = Counter(words)

    print("Total characters: ", len(text))
    print("Total words: ", len(words))
    print("Unique words: ", len(counts))
    print("\nTop 10 words: ")
    for w, c in counts.most_common(10):
        print(f"{w:<15} {c}")

def main():
    filename = input("Enter  text file path: ").strip()
    if not filename:
        print("No file provided. ")
        return
    try:
        analyze(filename)
    except FileNotFoundError:
        print("File not Found. ")
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()