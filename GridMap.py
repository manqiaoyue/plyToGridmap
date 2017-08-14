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
        
        #f(n) = g(n) + h(n)
        self.f = -1
        self.g = -1
        self.h = -1
        
    def __str__(self):
        position = "X:" + str(self.x) + " , Y:" + str(self.y)
        
        if self.n:
            n = 'N(' + str(self.n.x) + ', ' +str(self.n.y) + ') '
        else:
            n = "None "
            
        if self.e:
            e = 'E(' + str(self.e.x) + ', ' +str(self.e.y) + ') '
        else:
            e = "None "
            
        if self.s:
            s = 'S(' + str(self.s.x) + ', ' +str(self.s.y) + ') '
        else:
            s = "None "
            
        if self.w:
            w = 'W(' + str(self.w.x) + ', ' +str(self.w.y) + ')'
        else:
            w = "None"
            
        neighbors = n + e + s + w
        return position + '\n' + neighbors
    
    def cal_dist(self, x2, y2):
        dist = math.sqrt(pow((x2 - self.x), 2) + pow((y2 - self.y), 2))
        #print("DIST: " + str(dist))
        return dist
    
    
    def cal_direct(self, x2, y2):
        if(abs(x2 - self.x) > abs(y2 - self.y)): #east or west
            if x2 > self.x: #east
                if self.e == None:
                    self.e = Grid(self.x + 0.5, self.y)
                    self.e.w = self
                newGrid = self.e
                print("nowGrid : e" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
            else: #west
                if self.w == None:
                    self.w = Grid(self.x - 0.5, self.y)
                    self.w.e = self
                newGrid = self.w
                print("nowGrid : w" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
        else: #north or south
            if y2 > self.y: #north
                if self.n == None:
                    self.n = Grid(self.x, self.y + 0.5)
                    self.n.s = self
                newGrid = self.n
                print("nowGrid : n" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
            else: #south
                if self.s == None:
                    self.s = Grid(self.x, self.y - 0.5)
                    self.s.n = self
                newGrid = self.s
                print("nowGrid : s" + '(' + str(newGrid.x) + ',' + str(newGrid.y) + ')')
        return newGrid
    
    def cal_direct_for_grids(self, grid2):
        if(abs(grid2.x - self.x) > abs(grid2.y - self.y)): #east or west
            if grid2.x > self.x: #east
                self.e = grid2
                #print("Link to east grid")
            else: #west
                self.w = grid2
                #print("Link to west grid")
        else: #north or south
            if grid2.y > self.y: #north
                self.n = grid2
                #print("Link to north grid")
            else: #south
                self.s = grid2
                #print("Link to south grid")

class GridMap:
    def __init__(self, point_cloud, dataType='p'):
        ###dataType = 'p' : point cloud
        ###dataType = 'g' : grid map
        if len(point_cloud) < 1 or len(point_cloud[0]) < 2:
            return
        self.grids = []
        self.gridMap = []
        
        #add Grids
        for point in point_cloud:
            newGrid = Grid(point[0], point[1])
            self.addGrid(newGrid)
            
        #turn 2D point cloud to gridmap
        if dataType == 'p':
            #In this scope grid = point cloud , just differ on data structure
            nowGrid = self.grids[0]
            self.gridMap.append(nowGrid)    
            for grid in self.grids:
                dist = nowGrid.cal_dist(grid.x, grid.y)
                if  dist > GRID_SIZE and dist < MAX_DIST:
                    nowGrid = nowGrid.cal_direct(grid.x, grid.y)
                    if nowGrid not in self.gridMap:
                        self.gridMap.append(nowGrid)
                elif dist > MAX_DIST:
                    print("EXCEED MAX_DIST")
                    closestGrid = self.findClosestGrid(grid.x, grid.y)
                    dist = closestGrid.cal_dist(grid.x, grid.y)
                    if dist > GRID_SIZE:
                        #expend
                        nowGrid = closestGrid
                        print("---start expend---")
                        while dist > MAX_DIST:
                            nowGrid = nowGrid.cal_direct(grid.x, grid.y)
                            if nowGrid not in self.gridMap:
                                self.gridMap.append(nowGrid)
                            dist = nowGrid.cal_dist(grid.x, grid.y)
                        print("---end expend---")
                    else:
                        nowGrid = closestGrid.cal_direct(grid.x, grid.y)
                        if nowGrid not in self.gridMap:
                            self.gridMap.append(nowGrid)
        elif dataType == 'g':
            #In this scope grid is read from gridmap
            for grid in self.grids:
                for grid2 in self.grids:
                    if grid2 == grid:
                        continue
                    if grid.e == None or grid.w == None or grid.n == None or grid.s == None:
                        dist = grid.cal_dist(grid2.x, grid2.y)
                        if dist < 0.6:
                            grid.cal_direct_for_grids(grid2)
            self.gridMap = self.grids
                    
    
    def __str__(self):
        string = ""
        for grid in self.gridMap:
            string += '(' + str(grid.x) + ',' + str(grid.y) + ')\n'
        return string
    
    def addGrid(self, Grid):
        self.grids.append(Grid)
        
    def findClosestGrid(self, x2, y2):
        print("---Find Closest Points Start---")
        minDist = 999999
        minDistGrid = None
        
        for grid in self.gridMap:
            dist = grid.cal_dist(x2, y2)
            if minDist > dist:
                minDist = dist
                minDistGrid = grid
                
        if minDistGrid == None:
            print("Not Found")
            return self
        
        if minDist > MAX_DIST:
            print("Not Match Grid")

        
        print("Shortest Dist: " + str(minDist) + " , (" + str(minDistGrid.x) +"," + str(minDistGrid.y) + ")")
        print("---Find Closest Points End---")
        return minDistGrid
            
#    def buildMap(point_cloud):
#        for point in point_cloud:
#            if dist > GRID_SIZE:
#                search neighbors
#                if not neibors:
#                    newGRID
#                else:
#                    find the neighbor with dist < GRID_SIZE
                

        
        