import random
def code_generator():
    code = []
    while len(code) < 4: 
        number = random.randint(0,9)
        if number not in code:
            code.append(number)
    return code


def bulls_cows(guess):
    guess_code = []
    for number in guess:
        guess_code.append(int(number))
    print(f'\nYour guess: {guess_code}')
    bull = 0
    cow = 0
    for num in guess_code:
        if num in code:
            if guess_code.index(num) == code.index(num):
                bull = 1 + bull
            else:
                cow = 1 + cow
    return bull, cow


code = code_generator()
tries = 10

while tries > 0:
    guess = input("Guess the code: ")
    if len(guess) == 4 and guess.isdigit() and len(guess) == len(set(guess)):
        bull, cow = bulls_cows(guess)
        if bull == 4:
            print("You win!")
            tries = -1
        else:
            print(f'Bulls: {bull}, Cows: {cow}')
            tries = tries - 1
            print(f'remaining tries: {tries}\n')
    else:
        print("Sorry, please enter a valid 4 digit code, where numbers don't repeat")
if tries == 0:
    print(f"Sorry, you lose, the code was: {code}")