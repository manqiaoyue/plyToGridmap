import math

GRID_SIZE = 0.5
MAX_DIST = 0.8

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = None
        self.e = None
        self.s = None
        self.w = None
        
    def __str__(self):
        position = "X:" + str(self.x) + " , Y:" + str(self.y)
        
        if self.n:
            n = '(' + str(self.n.x) + ', ' +str(self.n.y) + ') '
        else:
            n = "None "
            
        if self.e:
            e = '(' + str(self.e.x) + ', ' +str(self.e.y) + ') '
        else:
            e = "None "
            
        if self.s:
            s = '(' + str(self.s.x) + ', ' +str(self.s.y) + ') '
        else:
            s = "None "
            
        if self.w:
            w = '(' + str(self.w.x) + ', ' +str(self.w.y) + ')'
        else:
            w = "None"
            
        neighbors = n + e + s + w
        return position + '\n' + neighbors
    
    def cal_dist(self, x2, y2):
        return math.sqrt(pow((x2 - self.x), 2) + pow((y2 - self.y), 2))
    
    
    def cal_direct(self, x2, y2):
        if(abs(x2 - self.x) > abs(y2 - self.y)): #east or west
            if x2 > self.x: #east
                self.e = Grid(self.x + 0.5, self.y)
                self.e.w = self
                newGrid = self.e
                print("newGrid : e" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
            else: #west
                self.w = Grid(self.x - 0.5, self.y)
                self.w.e = self
                newGrid = self.w
                print("newGrid : w" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
        else: #north or south
            if y2 > self.y: #north
                self.n = Grid(self.x, self.y + 0.5)
                self.n.s = self
                newGrid = self.n
                print("newGrid : n" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
            else: #south
                self.s = Grid(self.x, self.y - 0.5)
                self.s.n = self
                newGrid = self.s
                print("newGrid : s" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
        return newGrid

class GridMap:
    def __init__(self, point_cloud):
        if len(point_cloud) < 1 or len(point_cloud[0]) < 2:
            return
        self.grids = []
        self.gridMap = []
        
        #add Grids
        for point in point_cloud:
            newGrid = Grid(point[0], point[1])
            self.addGrid(newGrid)
            
        #build map
        nowGrid = self.grids[0]
        self.gridMap.append(nowGrid)    
        for grid in self.grids:
            dist = nowGrid.cal_dist(grid.x, grid.y)
            if  dist > GRID_SIZE and dist < MAX_DIST:
                nowGrid = nowGrid.cal_direct(grid.x, grid.y)
                if nowGrid not in self.gridMap:
                    self.gridMap.append(nowGrid)
            elif dist > MAX_DIST:
                closestGrid = self.findClosestGrid(grid.x, grid.y)
                if closestGrid == None:
                    #expend
                    pass
                else:
                    nowGrid = closestGrid.cal_direct(grid.x, grid.y)
                    if nowGrid not in self.gridMap:
                        self.gridMap.append(nowGrid)
        
        
    
    def __str__(self):
        string = ""
        for grid in self.gridMap:
            string += '(' + str(grid.x) + ',' + str(grid.y) + ')\n'
        return string
    
    def addGrid(self, Grid):
        self.grids.append(Grid)
        
    def findClosestGrid(self, x2, y2):
        minDist = 999999
        minDistGrid = None
        
        for grid in self.gridMap:
            dist = grid.cal_dist(x2, y2)
            if minDist > dist:
                minDist = dist
                minDistGrid = grid
                
        if minDist > MAX_DIST:
            minDistGrid = None
        
        return minDistGrid
            
#    def buildMap(point_cloud):
#        for point in point_cloud:
#            if dist > GRID_SIZE:
#                search neighbors
#                if not neibors:
#                    newGRID
#                else:
#                    find the neighbor with dist < GRID_SIZE
                

        
        