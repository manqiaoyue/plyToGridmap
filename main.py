# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
import copy

import ProcessPly as pp
import GridMap

###a star
def find_min_f(grids):
    minGrid = grids[0]
    
    for grid in grids:
        if grid.f < minGrid.f:
            minGrid = grid
    
    return minGrid

def search_neighbor(current, closed_list):
    if current.n == None or current.n in closed_list:
        pass
    else:
        
        

def a_star(grids, start, goal):
    closed_list = []
    open_list = [start] 
    
    #start g(n) = 0
    start.f = 0
    
    bool find_goal = False
    
    while not find_goal:
        current = find_min_f(open_list)
        
        if current.cal_dist(goal.x, goal.y) < GridMap.GRID_SIZE:
            return
        
        search_neighbor(current, closed_list)
        
        
        
        
    

points = []
x = []
y = []

for i in range(10):
    for j in range(10):
        points.append([j, i])
        x.append(j)
        y.append(i)
    

start = [0, 0]
goal = [9, 9]


gMap = GridMap.GridMap(points)
print("-----------------------------------------------------")
for i in range(50):
    print(i, gMap.gridMap[i])
    
gx = []
gy = []
for i in range(len(gMap.gridMap)):
    gx.append(gMap.gridMap[i].x)
    gy.append(gMap.gridMap[i].y)
    
#plot
plt.figure(figsize=(5, 5))
plt.axes = 'equal'
plt.scatter(x, y, c='green', s=5)
plt.scatter(gx, gy, c='red', s=2)


g1 = GridMap.Grid(0, 0)
g2 = GridMap.Grid(0, 0)
s = set()
s.update({g1, g2})
print(s)
print(g1 in s)
print(s{g1})





############### link grids ###################
#source = open("gridmap.txt", 'r')
#
#content = source.readlines()
#grids = []
#
#for item in content:
#    values = item.split(' ')
#    if len(values) < 2:
#        break
#    grids.append([float(values[0]), float(values[1])])
#
#source.close
#
#print(grids)
#print("Total Grids", len(grids))
#
#gMap = GridMap.GridMap(grids, dataType='g')
#
#x = []
#y = []
#for grid in grids:
#    x.append(grid[0])
#    y.append(grid[1])
#    
#gx = []
#gy = []
#for grid in gMap.gridMap:
#    gx.append(grid.x)
#    gy.append(grid.y)
#    
#plt.figure(figsize=(5, 5))
#plt.axis('equal')
#plt.scatter(x, y, c="green", s=8)
#plt.scatter(gx, gy, c="red", s=1)
#
#print(gMap.gridMap[0].n)
#print(gMap.gridMap[0].n.s)

###extract gripmap from 2D point cloud
#filename = "target.txt"
#source = open(filename, 'r')
#target = open("gridmap.txt", 'w')
#
#point_cloud = []
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
#        point_cloud.append([x, y])
#        
#
#gMap = GridMap.GridMap(point_cloud)
#print("2D points:", len(gMap.grids))
#print("GridMap Points:", len(gMap.gridMap))
#
#x = []
#y = []
#for point in point_cloud:
#    x.append(point[0])
#    y.append(point[1])
#   
#
#gx = []
#gy = []
#for grid in gMap.gridMap:
#    gx.append(grid.x)
#    gy.append(grid.y)
#   
#    
#plt.figure(figsize=(5, 5))
#plt.axis('equal')
#plt.scatter(x, y, c="green", s=2)
#plt.scatter(gx, gy, c="red", s=2)
#
##write file
#writed_num = 0
#for grid in gMap.gridMap:
#    string = str(grid.x) + " " + str(grid.y) + "\n"
#    target.write(string)
#    writed_num += 1
#print("writed num:", writed_num)
#
#source.close()
#target.close()


############### show point cloud ###############
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



############### process ply file ###############
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


