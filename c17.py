#17
'''
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = { i : set() for i in range(num_of_vertices) }
        self.visited = set()

    def addEdge(self, u, v, weightUV, weightVU):
        self.edges[u].add((v, weightUV))
        self.edges[v].add((u, weightVU))

    def getNeighbors(self, v):
        return self.edges[v]

def buildGraph(Grid):
    rows, cols = len(Grid), len(Grid[0])
    G = Graph(rows * cols)

    def neighbors(i, j):
        return tuple((x, y) for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if 0 <= x < rows and 0 <= y < cols)

    for i in range(rows):
        for j in range(cols):
            if i == j:
                continue
            for ni, nj in neighbors(i, j):
                G.addEdge(i * rows + j, ni * rows + nj, Grid[ni][nj], Grid[i][j])

    return G

def check(P, v, n, rows):
    if v not in P:
        return True
    prevNode1 = P[v]
    if prevNode1 not in P:
        return True
    prevNode2 = P[prevNode1]
    if prevNode2 not in P:
        return True
    prevNode3 = P[prevNode2]
    
    temp = tuple((node // rows, node % rows) for node in (n, v, prevNode1, prevNode2, prevNode3))
    if v == 3 and n == 4:
        print(temp)
    #if (all(temp[0][0] == x[0] for x in temp) or all(temp[0][1] == x[1] for x in temp)):
     #   print(temp)
    return not (all(temp[0][0] == x[0] for x in temp) or all(temp[0][1] == x[1] for x in temp))
    #not (direction == prevDir1 == prevDir2 == prevDir3)# == prevDir4)


from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    data: Any=field(compare=False)

def dijkstraRestricted(graph, start_vertex, rows):
    D = { v : float('inf') for v in range(graph.v) }

    D[start_vertex] = 0
    P = {}

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    
    while not pq.empty():
        #item = pq.get()
        dist, current_vertex = pq.get()#item.priority, item.data
        #graph.visited.add(current_vertex)

        for neighbor, distance in graph.getNeighbors(current_vertex):

            #if neighbor in graph.visited or not check(P, current_vertex, neighbor, rows):
                #continue
            

            old_cost = D[neighbor]
            new_cost = D[current_vertex] + distance

            if new_cost < old_cost:
                pq.put((new_cost, neighbor))
                D[neighbor] = new_cost
                P[neighbor] = current_vertex

    return D, P

def constructPath(node, P, path):
    if node in P:
        path.append(P[node])
        constructPath(P[node], P, path)

with open('i17.txt', 'r') as f:
    Grid = tuple(tuple(int(x) for x in row.strip()) for row in f)

G = buildGraph(Grid)
rows, cols = len(Grid), len(Grid[0])
start, target = 0, G.v - 1
D, P = dijkstraRestricted(G, start, rows)
path = [target]
constructPath(target, P, path)
print(D[target], tuple((node // rows, node % rows) for node in path[::-1]))'''

#not my code

import heapq
def minimal_heat(start, end, least, most):
    queue = [(0, *start, 0,0)]
    seen = set()
    while queue:
        heat,x,y,px,py = heapq.heappop(queue)
        if (x,y) == end: return heat
        if (x,y, px,py) in seen: continue
        seen.add((x,y, px,py))
        # calculate turns only
        for dx,dy in {(1,0),(0,1),(-1,0),(0,-1)}-{(px,py),(-px,-py)}:
            a,b,h = x,y,heat
            # enter 4-10 moves in the chosen direction
            for i in range(1,most+1):
                a,b=a+dx,b+dy
                if (a,b) in board:
                    h += board[a,b]
                    if i>=least:
                        heapq.heappush(queue, (h, a,b, dx,dy))

board = {(i,j): int(c) for i,r in enumerate(open('i17.txt')) for j,c in enumerate(r.strip())}
print(minimal_heat((0,0),max(board), 1, 3))
print(minimal_heat((0,0),max(board), 4, 10))
#
#