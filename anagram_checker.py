def anagram_check(word1, word2):
    word1_list = []
    word2_list = []
    length1 = len(word1)
    length2 = len(word2)
    counter = 0
    for letter in word1:
        word1_list.append(letter)
    for letter in word2:
        word2_list.append(letter)
    for letter in word1_list:
        if letter in word2_list:
            counter = counter + 1
    if counter == length2:
        print("This is an anagram")
    else:
        print("Not an anagram")

word1 = input("input a word: ").lower().replace(" ", "")
word2 = input("input a second word: ").lower().replace(" ", "")


if not word1.isalpha() or not word2.isalpha():
    print("Please enter a valid word (no numbers or special characters)")
    exit()
else:
    anagram_check(word1, word2)
