import random 

options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)

print("Welcome to a game of rock, paper scissors")
user_choice = input("Enter your choice: ").lower()

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win!")
elif user_choice == 'scissors' and computer_choice == 'rock':
    print("You lose")
elif user_choice == 'paper' and computer_choice == 'scissors':
    print("You lose")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win!")
elif user_choice == 'rock' and computer_choice == 'paper':
    print("You lose")
else:
    print("Invalid input, only choose between rock, paper, and scissors")
    exit()
print(f'You chose {user_choice}, and the computer chose {computer_choice}')