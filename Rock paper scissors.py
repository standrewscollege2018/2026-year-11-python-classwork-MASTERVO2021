'''Rock paper scissors'''

import random
#list of options
RPS = ['Rock', 'Paper', 'scissors']

#picking a random option
Option = random.choice(RPS)

#player option
player = input("Rock, paper or scissors?")

#comparing results
if Option == "Rock" and player == "Rock":
    print(f"Computer picks {Option}")
    print("Tie")

if Option == "Rock" and player == "Paper":
    print(f"Computer picks {Option}")
    print("You lose")

if Option == "Rock" and player == "Scissors":
    print(f"Computer picks {Option}")
    print("You win")

if Option == "Paper" and player == "Rock":
    print(f"Computer picks {Option}")
    print("You win")

if Option == "Paper" and player == "Paper":
    print(f"Computer picks {Option}")
    print("Tie")

if Option == "Paper" and player == "Scissors":
    print(f"Computer picks {Option}")
    print("You lose")

if Option == "Scissors" and player == "Rock":
    print(f"Computer picks {Option}")
    print("You lose")

if Option == "Scissors" and player == "Paper":
    print(f"Computer picks {Option}")
    print("You win")

if Option == "Scissors" and player == "Scissors":
    print(f"Computer picks {Option}")
    print("Tie")
