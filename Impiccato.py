import csv
csv_path = "Netflix-Shows/netflix_titles.csv"

with open(csv_path, newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=' ', quotechar='|')

    for row in csv_reader:
        print(row)
