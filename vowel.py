
vowels = ["a","e","i","o","u"]

def findVowels(word):
    vowelsInWord = []
    word = word.lower()
    if word.isalpha():
        for letter in word:
            if letter in vowels:
                vowelsInWord.append(letter)
        length = len(vowelsInWord)
        if length > 0:
            print(f"Your word has {length} vowels")
            print(vowelsInWord)
        else:
            print("None")
    else:
        print("Invalid Input")
    
findVowels("Hello")
findVowels("dhgddh")
findVowels("1233")
findVowels("MynameisBarbara")
findVowels("APPLES")

