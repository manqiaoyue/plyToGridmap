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
        
        #expend points
        for point in point_cloud:
            dist = self.cal_dist(nowPoint, point)
            if  dist > GRID_SIZE and dist < MAX_DIST:
                nowPoint = self.cal_direct(nowPoint, point)
                if nowPoint not in self.points:
                    self.points.append(nowPoint)
                    #print("Add newPoint")
            elif dist > MAX_DIST:
                closestPoint = self.findClosestPoint(point)
                closest_dist = self.cal_dist(closestPoint, point)
                if closest_dist > GRID_SIZE:
                    #print("Start expend------")
                    while closest_dist > GRID_SIZE:
                        closestPoint = self.cal_direct(closestPoint, point)
                        if closestPoint not in self.points:
                            self.points.append(closestPoint)
                        closest_dist = self.cal_dist(closestPoint, point)
                    #print("end expend------")
                nowPoint = closestPoint

        self.link_grids()
        
        for grid in self.gridmap:
            position = '(' + str(grid.x) + ', ' + str(grid.y) + ')\n'
            
            if grid.n:
                n = 'n(' + str(grid.n.x) + ', ' + str(grid.n.y) + ') '
            else:
                n = None
                
            if grid.e:
                e = 'e(' + str(grid.e.x) + ', ' + str(grid.e.y) + ') '
            else:
                e = None
                
            if grid.s:
                s = 's(' + str(grid.s.x) + ', ' + str(grid.s.y) + ') '
            else:
                s = None
                
            if grid.w:
                w = 'w(' + str(grid.w.x) + ', ' + str(grid.w.y) + ') '
            else:
                w = None
            print(position, n, e, s, w)


    
    def __str__(self):
        string = ""
        for grid in self.gridMap:
            string += '(' + str(grid.x) + ',' + str(grid.y) + ')\n'
        return string
    
        
    def findClosestPoint(self, p2):
        #print("---Find Closest Points Start---")
        minDist = 999999
        minDistPoint = None
        
        for point in self.points:
            dist = self.cal_dist(point, p2)
            if minDist > dist:
                minDist = dist
                minDistPoint = point
                
        if minDistPoint == None:
            #print("Not Found")
            return
        
        #if minDist > MAX_DIST:
            #print("Not Match Grid")
  
        #print("Shortest Dist: " + str(minDist) + " , (" + str(minDistPoint[0]) +"," + str(minDistPoint[1]) + ")")
        #print("---Find Closest Points End---")
        return minDistPoint
            
    def cal_dist(self, p1, p2):
        dist = math.sqrt(pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2))
        #print("DIST: " + str(dist))
        return dist
    
    def cal_direct(self, p1, p2):
        if(abs(p2[0] - p1[0]) > abs(p2[1] - p1[1])): #east or west
            if p2[0] > p1[0]: #east
                newPoint = [p1[0] + 0.5, p1[1]]
                #print("newPoint : e" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
            else: #west
                newPoint = [p1[0] - 0.5, p1[1]]
                #print("newPoint : w" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
        else: #north or south
            if p2[1] > p1[1]: #north
                newPoint = [p1[0], p1[1] + 0.5]
                #print("newPoint : n" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
            else: #south
                newPoint = [p1[0], p1[1] - 0.5]
                #print("newPoint : s" + '(' + str(newPoint[0]) + ',' + str(newPoint[1]) + ')')
        return newPoint
    
    def link_grids(self):
        for p1 in self.points:
            newGrid = self.search_gridmap(p1)
            if newGrid == None:
                newGrid = Grid(p1[0], p1[1])
                self.gridmap.append(newGrid)
                
            #search neighbors
            if newGrid.n == None:
                neighbor = self.search_neighbor('n', p1) 
                if neighbor:
                    neighbor_grid = self.search_gridmap(neighbor)
                    if neighbor_grid == None:
                        neighbor_grid = Grid(neighbor[0], neighbor[1])
                        newGrid.n = neighbor_grid
                        neighbor_grid.s = newGrid
                        self.gridmap.append(neighbor_grid)
                    else:
                        newGrid.n = neighbor_grid
                        neighbor_grid.s = newGrid
                        
            if newGrid.e == None:
                neighbor = self.search_neighbor('e', p1) 
                if neighbor:
                    neighbor_grid = self.search_gridmap(neighbor)
                    if neighbor_grid == None:
                        neighbor_grid = Grid(neighbor[0], neighbor[1])
                        newGrid.e = neighbor_grid
                        neighbor_grid.w = newGrid
                        self.gridmap.append(neighbor_grid)
                    else:
                        newGrid.e = neighbor_grid
                        neighbor_grid.w = newGrid
                        
            if newGrid.s == None:
                neighbor = self.search_neighbor('s', p1) 
                if neighbor:
                    neighbor_grid = self.search_gridmap(neighbor)
                    if neighbor_grid == None:
                        neighbor_grid = Grid(neighbor[0], neighbor[1])
                        newGrid.s = neighbor_grid
                        neighbor_grid.n = newGrid
                        self.gridmap.append(neighbor_grid)
                    else:
                        newGrid.s = neighbor_grid
                        neighbor_grid.n = newGrid
            
            if newGrid.w == None:
                neighbor = self.search_neighbor('w', p1) 
                if neighbor:
                    neighbor_grid = self.search_gridmap(neighbor)
                    if neighbor_grid == None:
                        neighbor_grid = Grid(neighbor[0], neighbor[1])
                        newGrid.w = neighbor_grid
                        neighbor_grid.e = newGrid
                        self.gridmap.append(neighbor_grid)
                    else:
                        newGrid.w = neighbor_grid
                        neighbor_grid.e = newGrid
            
    def search_gridmap(self, point):
        #check if the point in the gridmap
        nowGrid = None
        for grid in self.gridmap:
            if point[0] == grid.x and point[1] == grid.y:
                nowGrid = grid
        
        return nowGrid

    def search_neighbor(self, direction, p1):
        for point in self.points:
            if self.cal_dist(p1, point) == GRID_SIZE:
                if direction == 'n':
                    if p1[1] < point[1]:
                        return point
                elif direction == 'e':
                    if p1[0] < point[0]:
                        return point
                elif direction == 's':
                    if p1[1] > point[1]:
                        return point
                elif direction == 'w':
                    if p1[0] > point[0]:
                        return point
        return None
    

        
        