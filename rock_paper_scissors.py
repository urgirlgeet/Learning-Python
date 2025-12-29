# rock paper scissors game 
# practice random lib 

import random

options = ("rock", "paper", "scissors")
running = True

while running: 
    player = None
    code = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Code: {code}")

    if player == code:
        print("It's a tie")
    elif player == "rock" and code == "scissors":
        print("You win")
    elif player == "paper" and code == "rock":
        print("You win")
    elif player == "scissors" and code == "paper":
        print("You win")
    else:
        print("You lose")
    
    again = input("Do you want to play again? (y/n): ").lower()
    if not again == "y":
        running = False

print("Thanks for playing")