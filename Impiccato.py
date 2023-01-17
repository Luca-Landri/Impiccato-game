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
    return word

# The function that checks if the player has guessed the word
def word_guess(guess):
    if guess == word:
        return True
    else:
        return False

def letter_guess(guess):
    index = 0
    for letter in word:
        if letter == guess:
            censored[index] = letter            
        index += 1
    return censored
    
def game():
    while True:
        attemmp = 0
        print("_______________________________________________________")
        print("Benvenuto nel gioco dell'impiccato!")
        print("Il gioco consiste nel trovare la parola segreta, lettera per lettera.")
        print("Se sbagli troppi tentativi, il gioco finisce e il tuo amico verrà impiccato!")
        print("_______________________________________________________")
        print("La parola da indovinare è: ", *censored)
        print("che parola è?")
        player_guess = input()
        if word_guess(player_guess):
            print("Hai indovinato!")
        else:
            print("Hai sbagliato!")
            print("Prova ad indovinare una lettera")
            letter = input()
            letter_guess(letter)
            print(*censored)
            attemmp += 1
        if attemmp == 5:
            print("Hai finito i tentativi, il tuo amico verrà impiccato!")
            break


Films = read_csv()
word = random_word(Films)
print(word)
censored = censure_word(word)
game()