import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

G = 1

while G:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        G = 0
      
    if user_input not in options:
        continue
    
    randm_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[randm_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    
    else: 
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.") 
print("Computer won", computer_wins, "times.")   
print("Goodbye!")
