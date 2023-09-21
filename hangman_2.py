import random

with open("list_of_words.txt", "r") as file :
    words_list = [line.strip() for line in file]

word = random.choice(words_list)
blank_word = list(word)
for i in range (len(blank_word)) :
    blank_word[i] = "_"
player_count = 5

print(blank_word)

while player_count > 0 : 

    while "_" in blank_word :



        user_guess = str(input("Entrez une lettre : ")).upper()
        if len(user_guess) > 1 :
            print("Veuillez n'entrer qu'une seule lettre à la fois")
            continue

        found = False

        for j in range(len(word)) :
            if word[j] == user_guess and blank_word[j] == "_" :
                blank_word[j] = user_guess
                found = True 

        if not found :
            print("Lettre incorrecte. Vous perdez un point. Réessayez.")
            player_count -= 1
            print("Nombre de tentatives restantes : ", player_count)
            if player_count == 0 : 
                print("Vous avez perdu.")
                break

        print(blank_word)
    
    if "_" not in blank_word :
        print("Vous avez gagné champion ! Le mot était : ", word)
        break

print("Fin du jeu")

