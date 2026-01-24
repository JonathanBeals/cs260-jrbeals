import csv

with open('discharge.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        if (row[0] == "USGS"):
            print(', '.join(row))

print("Hello csci 260")