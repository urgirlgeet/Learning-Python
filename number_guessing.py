# number guessing game 
# practice random lib
import random

l_num = 1
h_num = 100
ans = random.randint(l_num, h_num)
guesses = 0
running = True

print("Number Guessing Game")
print(f"Guess a number between {l_num} and {h_num}")

while running:
    guess = input("Enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < l_num or guess > h_num:
            print("The number is out of range")
            print(f"Guess a number between {l_num} and {h_num}")
        elif guess > ans:
            print("Guess lower")
        elif guess < ans:
            print("Guess higher")
        else: 
            print(f"Correct guess, the answer was {ans}")
            print(f"It took you {guesses} guesses")
            running = False
    else: 
        print("Invalid guess")
        print(f"Guess a number between {l_num} and {h_num}")
