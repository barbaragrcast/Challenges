import random

def check_num(correct_num, guess):
    global game
    if guess <= 100 and guess >=1:
        if correct_num == guess:
            print("You Won!")
            game = False
        elif guess > correct_num:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    else:
        print("Your number is outside the range")

correct_num = random.randint(1, 100)

game = True
while game == True:
    guess = input("Guess a number between 1-100: ")
    try:
        guess = int(guess)
        check_num(correct_num, guess)
    except ValueError:
        print("Enter a valid number")