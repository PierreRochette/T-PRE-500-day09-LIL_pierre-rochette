import random

with open("list_of_words.txt", "r") as file :
    words_list = [line.strip() for line in file]

word = random.choice(words_list)
blank_word = list(word)
for i in range (len(blank_word)) :
    blank_word[i] = "_"

print(word)
print(blank_word)