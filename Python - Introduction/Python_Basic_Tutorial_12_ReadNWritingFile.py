# python tutorial writing and reading file
print("Tutorial 11 : Writing and Reading File")

# set a number in two column in format txt, called data.txt
fileName = 'data.txt'

inFile = open(fileName, 'r')    # open file for reading
line = inFile.readline()        # read first line

# x and y coordinates
# read x and y coordinate from file
x = []                          # define an empty array
y = []
for line in inFile:
    words = line.split()        # split line in to two words
    x.append(float(words[0]))   
    y.append(float(words[1]))
inFile.close()                  # close file
print(x)
print(y)

# transform y coordinates
from math import log

def f(y):
    return log(y)

for i in range(len(y)):
    y[i] = f(y[i])

print(y)

# write out x and y to two-column in file
fileName = 'data_out.txt'
outFile = open(fileName, 'w')   # open file for writing
outFile.write('# x and y coordinates\n')
for xi, yi in zip(x, y):
    outFile.write('%10.5f %10.5f\n' %(xi, yi))
outFile.close()                 # close file

# another methods loadtxt and savetxt
import numpy as np

# load text
data = np.loadtxt(fileName, comments='#')

x = data[:, 0]
y = data[:, 1]

data[:, 1] = np.log(y)

fileName = 'data_out2.txt'
outFile = open(fileName, 'w')   # open file for writing
outFile.write('# x and y coordinates\n')
np.savetxt(outFile, data, fmt='%10.5f')