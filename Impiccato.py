import csv
import random
player_guess = ""
letter = ""

# Function that reads the csv file and returns a list of films
def read_csv():
    filtered = []
    with open('./Dataset/netflix_titles.csv', encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["country"] == "Italy":
                filtered.append(row["title"])
    return filtered

# Function that censors the word
def censure_word(word):
    censored = []
    for letter in word:
        if letter == " ":
            censored.append(" ")
        else:
            censored.append("_")
        
    return censored

# The function that chooses a random word from the list
def random_word(films):
    word = random.choice(films)
    return word.lower()

# The function that checks if the player has guessed the word
def word_guess(guess):
    if guess == word.lower():
        return True
    else:
        return False

def letter_guess(guess):
    while True:
        if len(guess) > 1:
            print("Inserisci una sola lettera!")
        else:
            for i in range(len(word)):
                if guess == word[i]:
                    censored[i] = guess
            return censored
            break

def game():
    error = False
    attemmp = 5
    print("_______________________________________________________")
    print("Benvenuto nel gioco dell'impiccato!")
    print("Il gioco consiste nel trovare la parola segreta, lettera per lettera.")
    print("Se sbagli", attemmp, "tentativi, il gioco finisce e il tuo amico verrà impiccato!")
    print("_______________________________________________________")

    while True:
        if attemmp > 0:
            print("La parola da indovinare è: ", *censored)
            print("--Hai ancora", attemmp, "tentativi--")
            print("--Prova ad indovinare la parola intera--")
            while not error:
                player_guess = input()
                if len(player_guess) == 0:
                    print("ERR: Non puoi lasciare il campo vuoto!")
                else:
                    error = True
            if word_guess(player_guess):
                print("--BRAVISSIMO, HAI INDOVINATO!--")
                break
            else:
                print("--Hai sbagliato!", "Prova ad indovinare una lettera--")
                letter = input()
                letter_guess(letter)
                attemmp -= 1
        elif attemmp == 0:
            print("Hai finito i tentativi, il tuo amico verrà impiccato!")
            break


Films = read_csv()
word = random_word(Films)
print(word)
censored = censure_word(word)
game()