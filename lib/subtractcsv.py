#!/usr/bin/python
import sys, csv

file1=sys.argv[1]
file2=sys.argv[2]

valuesFile1 = []
reader = csv.reader(open(file1), delimiter=',')
for row in reader:
    try:
        if len(row) >= 1:
            valuesFile1.append(float(row[0]))
    except ValueError:
        pass


valuesFile2 = []
reader = csv.reader(open(file2), delimiter=',')
for row in reader:
    try:
        if len(row) >= 1:
            valuesFile2.append(float(row[0]))
    except ValueError:
        pass

for idx, val in enumerate(valuesFile1):
    val1 = val
    val2 = valuesFile2[idx]
    sub = val1-val2
    if sub < 0:
        sub = sub*-1
    print(sub)
