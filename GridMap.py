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
        
        self.parent = None
        
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


class GridMap:
    def __init__(self, point_cloud, dataType='p'):
        if len(point_cloud) < 1 or len(point_cloud[0]) < 2:
            return
        
        self.points = []
        self.gridmap = []
        
        ###TODO: first grid need to be normalized
        nowPoint = [point_cloud[0][0], point_cloud[0][1]]
        self.points.append(nowPoint)
        
        for point in point_cloud:
            dist = self.cal_dist(nowPoint, point)
            if  dist > GRID_SIZE and dist < MAX_DIST:
                nowPoint = self.cal_direct(nowPoint, point)
                if nowPoint not in self.points:
                    self.points.append(nowPoint)
                    print("Add newPoint")
            elif dist > MAX_DIST:
                closestPoint = self.findClosestPoint(point)
                closest_dist = self.cal_dist(closestPoint, point)
                if closest_dist > GRID_SIZE:
                    print("Start expend------")
                    while closest_dist > GRID_SIZE:
                        closestPoint = self.cal_direct(closestPoint, point)
                        if closestPoint not in self.points:
                            self.points.append(closestPoint)
                        closest_dist = self.cal_dist(closestPoint, point)
                    print("end expend------")
                nowPoint = closestPoint

        
#        ###dataType = 'p' : point cloud
#        ###dataType = 'g' : grid map
#        if len(point_cloud) < 1 or len(point_cloud[0]) < 2:
#            return
#        self.grids = []
#        self.gridMap = []
#        
#        #add Grids
#        for point in point_cloud:
#            newGrid = Grid(point[0], point[1])
#            self.addGrid(newGrid)
#            
#        #turn 2D point cloud to gridmap
#        if dataType == 'p':
#            #In this scope grid = point cloud , just differ on data structure
#            nowGrid = self.grids[0]
#            self.gridMap.append(nowGrid)    
#            for grid in self.grids:
#                dist = nowGrid.cal_dist(grid.x, grid.y)
#                if  dist > GRID_SIZE and dist < MAX_DIST:
#                    linkedGrid = nowGrid.cal_direct(grid.x, grid.y)
#                    if linkedGrid not in self.gridMap:
#                        self.gridMap.append(linkedGrid)
#                    nowGrid = linkedGrid
#                elif dist > MAX_DIST:
#                    print("EXCEED MAX_DIST")
#                    closestGrid = self.findClosestGrid(grid.x, grid.y)
#                    dist = closestGrid.cal_dist(grid.x, grid.y)
#                    if dist > GRID_SIZE:
#                        #expend
#                        nowGrid = closestGrid
#                        print("---start expend---")
#                        while dist > MAX_DIST:
#                            nowGrid = nowGrid.cal_direct(grid.x, grid.y)
#                            if nowGrid not in self.gridMap:
#                                self.gridMap.append(nowGrid)
#                            dist = nowGrid.cal_dist(grid.x, grid.y)
#                        print("---end expend---")
#                    else:
#                        nowGrid = closestGrid.cal_direct(grid.x, grid.y)
#                        if nowGrid not in self.gridMap:
#                            self.gridMap.append(nowGrid)
#        elif dataType == 'g':
#            #In this scope grid is read from gridmap
#            for grid in self.grids:
#                for grid2 in self.grids:
#                    if grid2 == grid:
#                        continue
#                    if grid.e == None or grid.w == None or grid.n == None or grid.s == None:
#                        dist = grid.cal_dist(grid2.x, grid2.y)
#                        if dist < 0.6:
#                            grid.cal_direct_for_grids(grid2)
#            self.gridMap = self.grids
                    
    
    def __str__(self):
        string = ""
        for grid in self.gridMap:
            string += '(' + str(grid.x) + ',' + str(grid.y) + ')\n'
        return string
    
    def addGrid(self, Grid):
        self.grids.append(Grid)
        
    def findClosestPoint(self, p2):
        print("---Find Closest Points Start---")
        minDist = 999999
        minDistPoint = None
        
        for point in self.points:
            dist = self.cal_dist(point, p2)
            if minDist > dist:
                minDist = dist
                minDistPoint = point
                
        if minDistPoint == None:
            print("Not Found")
            return
        
        if minDist > MAX_DIST:
            print("Not Match Grid")

        
        print("Shortest Dist: " + str(minDist) + " , (" + str(minDistPoint[0]) +"," + str(minDistPoint[1]) + ")")
        print("---Find Closest Points End---")
        return minDistPoint
            
    def cal_dist(self, p1, p2):
        dist = math.sqrt(pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2))
        print("DIST: " + str(dist))
        return dist
    
    def cal_direct(self, p1, p2):
        if(abs(p2[0] - p1[0]) > abs(p2[1] - p1[1])): #east or west
            if p2[0] > p1[0]: #east
                newPoint = [p1[0] + 0.5, p1[1]]
                print("newPoint : e" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
            else: #west
                newPoint = [p1[0] - 0.5, p1[1]]
                print("newPoint : w" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
        else: #north or south
            if p2[1] > p1[1]: #north
                newPoint = [p1[0], p1[1] + 0.5]
                print("newPoint : n" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
            else: #south
                newPoint = [p1[0], p1[1] - 0.5]
                print("newPoint : s" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
        return newPoint
    
#    def buildMap(point_cloud):
#        for point in point_cloud:
#            if dist > GRID_SIZE:
#                search neighbors
#                if not neibors:
#                    newGRID
#                else:
#                    find the neighbor with dist < GRID_SIZE
                

        
        