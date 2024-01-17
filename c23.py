# 23

import sys

sys.setrecursionlimit(10000)

with open('i23.txt') as f:
    lines = [ line.strip() for line in f ]

rows, cols = len(lines), len(lines[0])
startI, startJ = 0, lines[0].index('.')
endI, endJ = rows - 1, lines[-1].index('.')
counts = set()
visited = set()

def DFS(i, j, steps):
    if not (0 <= i < rows and 0 <= j < cols and lines[i][j] != '#' and (i, j) not in visited):
        return

    visited.add((i, j))

    if i == endI and j == endJ:
        counts.add(steps)
        visited.remove((i, j))
        return

    if (cell := lines[i][j]) == '^':
        DFS(i-1, j, steps + 1)
    elif cell == 'v':
        DFS(i+1, j, steps + 1)
    elif cell == '<':
        DFS(i, j-1, steps + 1)
    elif cell == '>':
        DFS(i, j+1, steps + 1)
    else:
        for nextI, nextJ in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
            DFS(nextI, nextJ, steps + 1)

    visited.remove((i, j))

DFS(startI, startJ, 0)

print(max(counts))

# 2 -------------------------------------------------------------------------------------------------

from collections import defaultdict

'''def topological_sort(graph):
    visited = set()
    sorted_nodes = []

    def visit(node):
        if node not in visited:
            visited.add(node)
            #print('A', node)
            for successor in graph[node]:
                visit(successor)
            #print('B', node)
            sorted_nodes.append(node)

    for node in list(graph):
        visit(node)

    return sorted_nodes[::-1]

def longest_path(graph, endNode):
    sorted_nodes = topological_sort(graph)
    dist = defaultdict(lambda: float('-inf'));print(sorted_nodes[0])
    dist[sorted_nodes[0]] = 0

    for node in sorted_nodes:
        for successor in graph[node]:
            dist[successor] = max(dist[successor], dist[node] + 1) #weights[(node, successor)]

    return dist[endNode]'''

Graph = defaultdict(set)

def DFS2(i, j, steps, prev):
    if not (0 <= i < rows and 0 <= j < cols and lines[i][j] != '#' and (i, j) not in visited):
        return

    visited.add((i, j))

    if (i == endI and j == endJ) or sum(int(0 <= ni < rows and 0 <= nj < cols and lines[ni][nj] != '#') for ni, nj in ((i+1, j), (i-1, j), (i, j-1), (i, j+1))) > 2:
        #if (prev, steps) not in Graph[(i, j)]:
        Graph[prev].add(((i, j), steps))
        steps = 0
        prev = (i, j)

    for nextI, nextJ in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
        DFS2(nextI, nextJ, steps + 1, prev)

    visited.remove((i, j))

visited.clear()
DFS2(startI, startJ, 0, (startI, startJ))

for k,v in Graph.items(): print(k,v)

'''def fix(Graph):
    newGraph = defaultdict(set)
    for key, nodes in list(Graph.items()):
        for node, steps in nodes:
            if (key, steps) not in Graph[node]:
                newGraph[key].add((node, steps))
    return newGraph

#Graph = fix(Graph)

#for k,v in Graph.items(): print(k,v)'''
Graph = {}
Graph[(0, 1)] = {((5, 3), 15)}
Graph[(5, 3)] = {((3, 11), 22), ((13, 5), 22)}
Graph[(13, 5)] = {((19, 13), 38), ((13, 13), 12)}
Graph[(19, 13)] = {((19, 19), 10), ((13, 13), 10)}
Graph[(13, 13)] = {((3, 11), 24), ((11, 21), 18)}
Graph[(3, 11)] = {((11, 21), 30)}
Graph[(11, 21)] = {((19, 19), 10)}
Graph[(19, 19)] = {((22, 21), 5)}

def DFS4(current, steps):
    if current in visited:
        return

    visited.add(current)

    if current == (endI, endJ):
        counts.add(steps)
        visited.remove(current)
        return

    for neighbor, nSteps in Graph[current]:
        DFS4(neighbor, steps + nSteps)

    visited.remove(current)

visited.clear()
counts.clear()
DFS4((startI, startJ), 0)
print(counts)




'''class Maze :
    
    def __init__(self) :
        self.length = -1
    
    #  Print grid elements
    def printPath(self, grid, row, col) :
        #  Loop controlling variables
        i = 0
        j = 0
        while (i < row) :
            j = 0
            while (j < col) :
                print("", grid[i][j] ,end = "\t")
                j += 1
            
            print()
            i += 1
        
        print()
    
    #  Copy visitor element to output collection
    def copyResult(self, visitor, output, row, col) :
        #  Loop controlling variables
        i = 0
        j = 0
        while (i < row) :
            j = 0
            while (j < col) :
                #  Assign element
                output[i][j] = visitor[i][j]
                j += 1
            
            i += 1
        
    
    #  Find all paths which is exist in given source to destination position
    #  r and c is Source point
    #  x and y is destination point
    def findPath(self, collection, visitor, output, r, c, x, y, counter, row, col) :
        if (r < 0 or r >= row or c < 0 or c >= col) :
            # When not valid position
            return 
        
        elif(r == x and c == y) :
            # When we get destination position
            if (visitor[r][c] == 0 and self.length < counter) :
                self.length = counter
                self.copyResult(visitor, output, row, col)
                # When destination are active element
                output[r][c] = counter + 1
            
        
        if (visitor[r][c] != 0) :
            # When the element has been already been visited
            return 
        
        if (collection[r][c] == 1) :
            # Active visiting node
            visitor[r][c] = counter + 1
            # Test four possible direction
            self.findPath(collection, visitor, output, r + 1, c, x, y, counter + 1, row, col)
            self.findPath(collection, visitor, output, r, c + 1, x, y, counter + 1, row, col)
            self.findPath(collection, visitor, output, r - 1, c, x, y, counter + 1, row, col)
            self.findPath(collection, visitor, output, r, c - 1, x, y, counter + 1, row, col)
            #  Deactivate visited node status
            visitor[r][c] = 0

    
    # Handles the request to find maze solution
    #  r and c is Source point
    #  x and y is destination point
    def longestPath(self, collection, r, c, x, y, row, col) :
        #  x and y destination point
        if (x < 0 or x >= row or y < 0 or y >= col) :
            return
        
        #  r and c Source point
        if (r < 0 or r >= row or c < 0 or c >= col) :
            return
        
        elif(collection[r][c] == 0) :
            print("\n Source are not active ")
        
        elif(collection[x][y] == 0) :
            print("\n Destination are not active ")
        
        # Create resultant grid
        output = [[0] * (col) for _ in range(row) ]
        visitor = [[0] * (col) for _ in range(row) ]
        self.length = -1
        self.findPath(collection, visitor, output, r, c, x, y, 0, row, col)
        if (self.length != -1) :
            # When result are exist
            print("\n Source point (", r ,",", c ,") Destination point (", x ,",", y ,") ", end = "")
            #  Display output solution
            print("\n Longest Path ")
            #self.printPath(output, row, col)
            print(max(max(line) for line in output) - 1)
        else :
            # When no solution possible
            print("\n No Result ")

task = Maze()
collection = [ [int(c != '#') for c in line] for line in lines ]

#  Get size
row = len(collection)
col = len(collection[0])
#  Print input problem
task.longestPath(collection, startI, startJ, endI, endJ, row, col)'''