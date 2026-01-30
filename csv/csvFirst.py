import csv
import math

with open('discharge.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    i = 0
    total = 0
    totalSquare=0
    count = 0
    maxVal = 0
    minVal = 0
    first = True
    for row in spamreader:
        if (row[0] == "USGS" and i < 100 ):
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

print(f"Average: , {total/count:.2f}")
stdev = math.sqrt((totalSquare-total*total/count)/(count -1))
print(f"Std Dev: , {stdev:>6.2f}")
print(f"Min:, \t{minVal:>10.2f}")
print(f"Max:, \t{maxVal:>10.2f}")