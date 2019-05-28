#!/usr/bin/python
import sys, csv
import numpy

def getValues(filename):
    values = []
    reader = csv.reader(open(filename), delimiter=',')
    for row in reader:
        try:
            if len(row) >= 1:
                values.append(float(row[0]))
        except ValueError:
            pass
    return values

# read in all specified files
valuesPerFile=[]
for i in range(1, len(sys.argv)):
    filename = sys.argv[i]
    values = getValues(filename)
    valuesPerFile.append(values)

valuesFirstFile=valuesPerFile[0]
for idx, val in enumerate(valuesFirstFile):
    timestampValues = []
    for fileValues in valuesPerFile:
        timestampValues.append(fileValues[idx])

    avg = numpy.average(timestampValues, axis=0)
    std = numpy.std(timestampValues, axis=0)
    print("%d %d" % (avg, std))
