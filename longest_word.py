def longest_word_finder(sentence):
    sentence = sentence.split()
    i = 1
    for word in sentence:
        length = len(word)
        if length > i:
            greatest = word
            i = length
    print(f'The longest word is "{greatest}" with the length of {i} letters.')

sentence = input("Enter a sentence: ")
longest_word_finder(sentence)
