import csv
import random

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
    censored = ""
    for letter in word:
        if letter == " ":
            censored += " "
        else:
            censored += "_"
        
    return censored

# The function that chooses a random word from the list
def random_word(films):
    word = random.choice(films)
    return word

# The function that checks if the player has guessed the word
def word_guess(guess):
    if guess == word:
        return True
    else:
        return False
    

Films = read_csv()
word = random_word(Films)
print(word)
censored = censure_word(word)
attemp = 5
player_guess = ""


def game():
    print("_______________________________________________________")
    print("Benvenuto nel gioco dell'impiccato!")
    print("Il gioco consiste nel trovare la parola segreta, lettera per lettera.")
    print("Se sbagli troppi tentativi, il gioco finisce e il tuo amico verrà impiccato!")
    print("_______________________________________________________")
    print("La parola da indovinare è: ", censored)
    print("Hai ", attemp, " tentativi", "che parola è?")
    player_guess = input()
    if word_guess(player_guess):
        print("Hai indovinato!")



game()