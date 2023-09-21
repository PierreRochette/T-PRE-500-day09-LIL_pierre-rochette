import random

words_list = ['HELLO', 'GOODBYE', 'WORLD', 'MARS', 'EARTH', 'PLEASE', 'WAREHOUSE', 'ANTICONSTITUTIONNELLEMENT', "HIPPOPOTOMONSTROSESQUIPEDALIOPHOBIE", "EPITECH"]
word = words_list[random.randint(0, len(words_list) - 1)]
blank_word = list(word)
player_count = len(blank_word)
for i in range(len(blank_word)) :
    blank_word[i] = "_"
print(blank_word)


# Tout fait l'effet attendu jusqu'ici. 

while player_count > 0 : 

    while "_" in blank_word :

        user_guess = str(input("Entrez une lettre : ")).upper()
        if len(user_guess) > 1 :
            print("Veuillez n'entrer qu'une seule lettre à la fois.")
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
        print("Vous avez gagné champion ! Le mot était : ", "".join(blank_word))
        break

print("Fin du jeu")