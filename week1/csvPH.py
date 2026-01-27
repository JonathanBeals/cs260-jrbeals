import csv
import math

i = 0
total = 0
totalSquare = 0
count = 0
maxVal = 0
minVal = 0
first = True

with open('pH.txt', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        if (row[0] == "USGS"):
            total += float(row[4])
            value = float(row[4])
            totalSquare += value * value
            if first:
                maxVal = value
                minVal = value
                first = False
            else:
                if maxVal < value:
                    maxVal = value
                if minVal > value:
                    minVal = value
            count += 1

stdev = math.sqrt((totalSquare-total*total/count)/(count -1))
print(f"Min: \t{minVal:>7.2f}")
print(f"Max: \t{maxVal:>7.2f}")
print(f"Average: {total/count:>6.2f}")
print(f"Std Dev: {stdev:>6.2f}")