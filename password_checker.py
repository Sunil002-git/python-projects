import string

def check_password(pw: str):
    length_ok = len(pw) >= 8
    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(c in string.punctuation for c in pw)

    score = sum([length_ok, has_lower, has_upper, has_digit, has_symbol])

    if score <= 2:
        level = 'Weak'
    elif score == 3 or score == 4:
        level = 'Medium'
    else:
        level = 'Strong'
    
    return level, {
        "length>=8": length_ok,
        "lowercase" : has_lower,
        "uppercase": has_upper,
        "digit" : has_digit,
        "symbol" : has_symbol
    }

def main():
    pw = input("Enter You Password: ")
    level, details = check_password(pw)
    print("Strength: ", level)
    for k, v in details.items():
        print(f"{k} : {'Ok' if v else 'Missing'}")

if __name__ == "__main__":
    main()

# any(iterables) returns true or false
# import string 
# string.punctuation