import string

def unique_word_counter(sentence):
    if sentence.isdigit() == False and sentence != "":
        sentence = sentence.lower()
        sentence = sentence.translate(str.maketrans("", "", string.punctuation))
        words = sentence.split()

        total = len(words)
        repeated = []

        for word in words:
            if words.count(word) > 1 and word not in repeated:
                repeated.append(word)

        print(f"Total words: {total}, Repeated words (unique): {len(repeated)}")
    else:
        print("invalid, please enter a valid sentence")


sentence = input("Please enter a sentence: ")
unique_word_counter(sentence)