import csv

with open('data.csv') as csvfile:
    filedata = csv.reader(csvfile)
    for line in filedata:
        print(line)