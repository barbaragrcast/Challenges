def acronym_generator(phrase):
    first_letter = []
    phrase = phrase.title()
    for letter in phrase:
            if letter.isupper():
                first_letter.append(letter)
    length = len(first_letter)
    if length == 1:
        print("Sorry, your phrase is too short")
    else:
        acronym = ''.join(first_letter)
        print(acronym)



phrase = input('Enter phrase to make an acronym: ')

acronym_generator(phrase)