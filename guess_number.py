# import random

# def play():
#     secret = random.randint(1, 100)
#     tries = 0
#     print("I'm Guessing of a number between 1 and 100. ")
    
#     while True:
#         guess_str = input("Your Guess: ").strip()
#         if not guess_str.isdigit():
#             print("Please enter a whole number. ")
#             continue

#         guess = int(guess_str)
#         tries += 1
        
#         if guess < secret:
#             print("Too Low")
#         elif guess > secret:
#             print("Too high")
#         else:
#             print(f"Correct! You guessed it in {tries} tries. ")
#             break


# if __name__ == "__main__":
#     play()

for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
