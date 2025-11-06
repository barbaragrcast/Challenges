def check_palindrome(word):
    letter_list = []
    reversed_list =[]
    for char in word:
        letter_list.append(char)
    length = len(letter_list)
    length = -length
    i= -1
    while i >= length: 
        reversed_list.append(letter_list[i])
        i = i-1
    
    if letter_list == reversed_list:
        print("This word is a palindrome")
    elif letter_list != reversed_list:
        print("This word is not a palindrome")

word_choice = input("Enter a word: ").lower().strip()

check_palindrome(word_choice)
