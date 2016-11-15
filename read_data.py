import csv

with open('data_10_50_100.txt', 'rb') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        print row, len(row)
        break