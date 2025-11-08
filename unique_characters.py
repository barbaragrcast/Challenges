def check_unique_char(word):
    char_list = []
    for char in word:
        char_list.append(char)
    
    length = len(char_list)
    
    for i in range(length):
        for j in range(i+1, length):  
            if char_list[i] == char_list[j]:
                print(f"The letter {char_list[i]} repeats")
                return  

    print("all letters are unique")

word = input("Enter a word: ").lower()
if word.isdigit():
    print("Please enter a valid word")
else:
    check_unique_char(word)