# -*- coding: utf-8 -*-
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
            if len(value) < 6:
                #if read the face indeices
                continue
            zPoints.append(float(value[2]))
            if float(value[2]) > -1.40 and float(value[2]) < -1.2:
                #                value1                      value2
                #modify these value to adjust threshold
                points.append(item)
        
    #modify header
    for idx in range(len(header)):
        if header[idx].find('element vertex') >= 0:
            elements = header[idx].split(' ')
            elements[2] = str(len(points)) + '\n'
            header[idx] = elements[0] + ' ' + elements[1] + ' ' + elements[2]
        elif header[idx].find('element face') >= 0:
            elements = header[idx].split(' ')
            elements[2] = str(0) + '\n'
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