import csv
import random

# Funzione per la lettura del file csv
def read_csv():
    filtered = []
    with open('./Dataset/netflix_titles.csv', encoding="utf8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["country"] == "Italy":
                filtered.append(row["title"])
    return filtered

Films = read_csv()

print(Films)
