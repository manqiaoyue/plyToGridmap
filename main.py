# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
import math

import ProcessPly as pp
import GridMap


############### A star ###################
#def find_min_f(grids):
#    minGrid = grids[0]
#    
#    for grid in grids:
#        if grid.f < minGrid.f:
#            minGrid = grid
#    
#    return minGrid
#
#def cal_f(n_grid, goal):
#    return abs(n_grid.x - goal.x) + abs(n_grid.y - goal.y)
#
#def cal_g(n_grid, neighbor_grid):
#    dist = neighbor_grid.g + 0.5 #0.5 is GRI_SIZE
#    if dist < n_grid.g:
#        n_grid.g = dist
#        n_grid.f = n_grid.g + n_grid.h
#    
#
#def search_neighbor(current, open_list, closed_list):
#    if current.n == None or current.n in closed_list:
#        pass
#    else:
#        n_to_neighbor_dist = cal_g(current, current.n)
#        if n_to_neighbor_dist < current.n.g or current.n not in open_list:
#            current.n.g = n_to_neighbor_dist
#            current.n.f = cal_f(current.n, goal)
#            current.n.parent = current
#        if current.n not in open_list:
#            open_list.append(current.n)
#        
#    if current.e == None or current.e in closed_list:
#        pass
#    else:
#        n_to_neighbor_dist = cal_g(current, current.e)
#        if n_to_neighbor_dist < current.e.g or current.e not in open_list:        
#            current.e.g = n_to_neighbor_dist
#            current.e.f = cal_f(current.e, goal)
#            current.e.parent = current
#        if current.e not in open_list:
#            open_list.append(current.e)
#        
#    if current.s == None or current.s in closed_list:
#        pass
#    else:
#        n_to_neighbor_dist = cal_g(current, current.s)
#        if n_to_neighbor_dist < current.s.g or current.s not in open_list:        
#            current.s.g = n_to_neighbor_dist
#            current.s.f = cal_f(current.s, goal)
#            current.s.parent = current
#        if current.s not in open_list:
#            open_list.append(current.s)
#        
#    if current.w == None or current.w in closed_list:
#        pass
#    else:
#        n_to_neighbor_dist = cal_g(current, current.w)
#        if n_to_neighbor_dist < current.w.g or current.w not in open_list:        
#            current.w.g = n_to_neighbor_dist
#            current.w.f = cal_f(current.w, goal)
#            current.w.parent = current
#        if current.w not in open_list:
#            open_list.append(current.w)
#        
#
#def a_star(grids, start, goal):
#    closed_list = []
#    open_list = []
#    
#    start.g = 0
#    start.h = cal_f(start, goal)
#    start.f = start.g + start.h
#    open_list.append(start)
#    
#    find_goal = False
#    
#    while not find_goal:
#        current = find_min_f(open_list)
#        #remove current from open
#        #add current to closed
#        
#        if current.cal_dist(goal.x, goal.y) < GridMap.GRID_SIZE:
#            return
#        
#        search_neighbor(current, open_list, closed_list)
      
    
### test gridmap with predefined points        
#points = [[0, 0], [0.3, 0], [0.6, 0], [1.9, 0], [0, 0.3], [0, 2.9], [-5, -7]]
#x = []
#y = []
#
#for point in points:
#    x.append(point[0])
#    y.append(point[1])
#    
#gMap = GridMap.GridMap(points)
#
#gx = []
#gy = []
#
#for point in gMap.points:
#    gx.append(point[0])
#    gy.append(point[1])
#
##plot
##plt.figure(figsize=(5, 5))
#plt.axes = 'equal'
#plt.scatter(x, y, c='green', s=6)
#plt.scatter(gx, gy, c='red', s=3)


### test gridmap with 10 x 10 points
#points = []
#x = []
#y = []
#
#for i in range(100):
#    for j in range(100):
#        points.append([j/10, i/10])
#        x.append(j/10)
#        y.append(i/10)
#
#
#gMap = GridMap.GridMap(points)
#print("-----------------------------------------------------")
#print("GRID POINTS:", len(gMap.points))
#gx = []
#gy = []
#for i in range(len(gMap.points)):
#    gx.append(gMap.points[i][0])
#    gy.append(gMap.points[i][1])
#    
####plot
#plt.figure(figsize=(5, 5))
#plt.axes = 'equal'
#plt.scatter(x, y, c='green', s=1)
#plt.scatter(gx, gy, c='red', s=2)


### test gridmap with processed point cloud
filename = "target.txt"
source = open(filename, 'r')

points = []
x = []
y = []
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
        x0 = float(values[0])
        y0 = float(values[1])
        x.append(x0)
        y.append(y0)
        points.append([x0, y0])
        
print(len(points))

gMap = GridMap.GridMap(points)
print("GRID POINTS:", len(gMap.points))
gx = []
gy = []
for i in range(len(gMap.points)):
    gx.append(gMap.points[i][0])
    gy.append(gMap.points[i][1])
    
###plot
plt.figure(figsize=[5, 10])
plt.axis = 'equal'
plt.scatter(x, y, c='green',s=0.1)
plt.scatter(gx, gy, c='red', s=2)



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
###the processed point cloud will output as "target.txt"
#filename = "lab2.ply"
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
##plt.axis([-2, 2, 0, 100000])
#plt.grid(True)
#
#plt.show()


