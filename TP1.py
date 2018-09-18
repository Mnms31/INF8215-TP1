import numpy as np

def read_graph():
    return np.loadtxt("montreal", dtype='i', delimiter=',')

graph = read_graph()

import copy

class Solution:
    def __init__(self, places, graph):
        """
        places: a list containing the indices of attractions to visit
        p1 = places[0]
        pm = places[-1]
        """
        self.g = 0 # current cost
        self.graph = graph 
        self.visited = [places[0]] # list of already visited attractions
        self.not_visited = copy.deepcopy(places[1:]) # list of attractions not yet visited
        
    def add(self, idx):
    
        self.g+=self.graph[self.visited[-1],self.not_visited[idx]]
        self.visited.append(self.not_visited[idx])
        self.not_visited.pop(idx)
        
        """
        
        
        Adds the point in position idx of not_visited list to the solution
        """
        
"""def bfs(graph, places):
    solCourante = Solution(places,graph)
    file = [solCourante]
    while solCourante.add() :
      
        
import time 

#test 1  --------------  OPT. SOL. = 27
start_time = time.time()
places=[0, 5, 13, 16, 6, 9, 4]
sol = bfs(graph=graph, places=places)
print(sol.g)
print("--- %s seconds ---" % (time.time() - start_time))
"""

def fastest_path_estimation(sol) :
    solLocale = sol
    c = sol.visited[-1]
    pm = sol.not_visited[-1]
    fDijkstra = [0]+[10000 for i in range(len(sol.not_visited))]
    while c!=pm :
        min = 10000
        poids = 0
        indexMin = 0
        for i in range(len(solLocale.not_visited)) :
            poids = fDijkstra[i]
            if poids < min :
                solLocale.append(solLocale.not_visited[i])
                min = poids
                indexMin = i
        solLocale.add(sol.not_visited(i))
        for j in range(len(solLocale.not_visited)) :
            if fDijkstra[j] > (fDijkstra[indexMin] + solLocale.graph[indexMin,j]) :
                fDijkstra[j] = fDijkstra[indexMin] + solLocale.graph[indexMin,j]
    return solLocale.g
            

import heapq
def A_star(graph, places):
    """
    Performs the A* algorithm
    """
    # blank solution
    root = Solution(graph=graph, places=places)
    # search tree T
    T = []
    heapq.heapify(T)
    heapq.heappush(T, root)
        
    
        
            
        