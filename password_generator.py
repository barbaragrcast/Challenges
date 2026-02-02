import random
import string

allowed_attributes = ["uppercase","lowercase", "digits", "symbols"]
def password_generator(length, attributes):
    invalid = []
    characters = []
    required = []
    attributes = attributes.split(",")
    attributes = [char.strip() for char in attributes]
    for attribute in attributes:
        if attribute not in allowed_attributes:
            invalid.append(attribute) 
        elif attribute == "uppercase":
            characters.append(string.ascii_uppercase)
            required.append(random.choice(string.ascii_uppercase))
        elif attribute == "lowercase":
            characters.append(string.ascii_lowercase)
            required.append(random.choice(string.ascii_lowercase))
        elif attribute == "digits":
            characters.append(string.digits)
            required.append(random.choice(string.digits))
        elif attribute == "symbols":
            characters.append(string.punctuation)
            required.append(random.choice(string.punctuation))
    if invalid or length < 4:
        print("Invalid input or length less than 4")
    else:
        if length < len(required):
            print("Password length too short for selected attributes")
            return
        characters = "".join(characters)
        remaining = length - len(required)
        password = required + random.choices(characters, k=remaining)
        random.shuffle(password)
        password = "".join(password)
        print(f"Generated password: {password}")


length = input("Length of desired password: ")
try:
    length = int(length)
    attributes = input("Please enter wanted attributes seperated by a comma (allowed attributes: digits, symbols, uppercase, lowercase): ").lower()
    password_generator(length, attributes)
except ValueError:
    print("Sorry, invalud number or attribute")
