# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

def getZ(string):
    string = string.split(' ')
    return string

def readPly(filename):
    source = open(filename, 'r')
    target = open('target.txt', 'w')
    
    header = []
    zPoints = []
    points = []
    content = source.readlines()
    
    foundHeaderEnd = False
    for item in content:
        if not foundHeaderEnd:
            header.append(item)
            if item == "end_header\n":
                foundHeaderEnd = True
        else:
            value = getZ(item)
            zPoints.append(float(value[2]))
            if float(value[2]) > -1.50 and float(value[2]) < -1.0:
                points.append(item)
        
    #modify header
    for idx in range(len(header)):
        if header[idx].find('vertex') >= 0:
            elements = header[idx].split(' ')
            elements[2] = str(len(points)) + '\n'
            header[idx] = elements[0] + ' ' + elements[1] + ' ' + elements[2]
    
    #write header
    for item in header:
        target.write(item)
    #write points
    for item in points:
        target.write(item)
    
    source.close()
    target.close()
    
    return zPoints


### Main ###
filename = "file.txt"
zPoints = readPly(filename)

#plot
x = zPoints

# the histogram of the data
plt.hist(x, 50, normed=0, facecolor='green', alpha=0.75)

plt.xlabel('Value')
plt.ylabel('Count')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([-2, 2, 0, 100000])
plt.grid(True)

plt.show()

