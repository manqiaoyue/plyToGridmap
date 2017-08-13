# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

import ProcessPly as pp
import GridMap

###test class
#point_cloud = [[0.0, 0.0], [0, .4], [0, .7], [.4, 0], [.6, 0], [-7, -5]]
filename = "target.txt"
source = open(filename, 'r')

point_cloud = []
content = source.readlines()

foundHeaderEnd = False
for item in content:
    if not foundHeaderEnd:
        if item == "end_header\n":
            foundHeaderEnd = True
    else:
        values = item.split(' ')
        if len(values) < 2:
            break
        x = float(values[0])
        y = float(values[1])
        point_cloud.append([x, y])
        

gMap = GridMap.GridMap(point_cloud)
print("2D points:", len(gMap.grids))
print("GridMap Points:", len(gMap.gridMap))

x = []
y = []
for point in point_cloud:
    x.append(point[0])
    y.append(point[1])
   
#plt.figure(figsize=(5, 5))
#plt.scatter(x, y)

gx = []
gy = []
for grid in gMap.gridMap:
    gx.append(grid.x)
    gy.append(grid.y)
   
    
plt.figure(figsize=(5, 5))
plt.axis('equal')
plt.scatter(x, y, c="green", s=2)
plt.scatter(gx, gy, c="red", s=2)

#plt.figure(figsize=(5, 5))
#plt.scatter(gx, gy)





###show point cloud
#filename = "target.txt"
#source = open(filename, 'r')
#
#points = []
#content = source.readlines()
#
#foundHeaderEnd = False
#for item in content:
#    if not foundHeaderEnd:
#        if item == "end_header\n":
#            foundHeaderEnd = True
#    else:
#        values = item.split(' ')
#        if len(values) < 2:
#            break
#        x = float(values[0])
#        y = float(values[1])
#        points.append([x, y])
#        
#print(points)
#print(len(points))
#
##plot
#plt.figure(figsize=(8,12))
#x = []
#y = []
#for point in points:
#    x.append(point[0])
#    y.append(point[1])
#    
#plt.scatter(x, y, s=0.1)
#plt.show()



###process ply file
#filename = "file.txt"
#zPoints = pp.readPly(filename)
#
##plot
#x = zPoints
#
## the histogram of the data
#plt.hist(x, 50, normed=0, facecolor='green', alpha=0.75)
#
#plt.xlabel('Value')
#plt.ylabel('Count')
#plt.title("Distribute of Z values")
#plt.axis([-2, 2, 0, 100000])
#plt.grid(True)
#
#plt.show()


