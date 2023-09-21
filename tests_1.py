import random

with open("list_of_words.txt", "r") as file :
    words_list = [line.strip() for line in file]

word = random.choice(words_list)
blank_word = "_" * len(word)
player_count = 5




user_guess = str(input("Entrez une lettre :")).upper()

if len(user_guess) == 1 : 
    for i in range(len(word)) :
        if word[i] == user_guess and blank_word[i] == "_" :
            blank_word[i].replace("_", user_guess)


print(blank_word)

