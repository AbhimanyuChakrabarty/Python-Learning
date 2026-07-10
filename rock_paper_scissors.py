print("Welcome to rock, paper, scissors")

user_choice = str(input("what do you choose? 'Rock', 'Paper', or 'Scissors' \n")).lower()

import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

if user_choice == "rock" and computer_choice == "paper":
    print("paper smashes rock, you lose!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("rock smashes scissors, you win!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("scissors cut paper, you lose!")
elif user_choice == "paper" and computer_choice == "rock":
    print("paper covers rock, you win!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("rock smashes scissors, you lose!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("scissors cut paper, you win!")
else:
    print("It's a tie!")
