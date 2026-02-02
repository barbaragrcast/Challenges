import string

def url_slug(sentence):
    counter = 0
    characters = []
    sentence = sentence.lower()
    for char in sentence:
        characters.append(char)
        if char in string.punctuation:
            counter += 1
    length = len(characters)

    if sentence == "" or length == counter:
        print("Sorry, invalid. Your input was either empty or all special characters")
    else:
        sentence = sentence.translate(str.maketrans('','',string.punctuation))
        sentence = sentence.translate(str.maketrans(' ','-',string.punctuation))
        print(sentence)



sentence = input("Enter a sentence: ")
url_slug(sentence)