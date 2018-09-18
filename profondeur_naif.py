# TP1 INF8215

import numpy as np
import copy
from queue import Queue

def read_graph():
    return np.loadtxt("montreal", dtype='i', delimiter=',')

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
        """
        Adds the point in position idx of not_visited list to the solution
        """
        self.g += self.graph[self.visited[-1], self.not_visited[idx]]
        self.visited.append(self.not_visited[idx])
        del self.not_visited[idx]
        
    def __add__(self, other):
        #if self.graph != other.graph:
        #    print("error")
        s = Solution(self.visited + other.visited, self.graph)
        #print("self.g " + str(self.g))
        #print("other.g " + str(other.g))
        #print("self.graph[self.visited[-1], other.visited[0]] " + str(self.graph[self.visited[-1], other.visited[0]]))
        s.g = self.g + other.g + self.graph[self.visited[-1], other.visited[0]]
        return s
 
def bfs(graph, places):
    if len(places) == 2:
        s = Solution(places, graph)
        s.add(0)
        return s
    else:
        s_tab = []
        sol_init = Solution([places[0]], graph) # etat initial
        
        for i in range(1-1, len(places)-2):
            pl_rec = places.copy()[1:]
            temp = pl_rec[0]
            pl_rec[0] = pl_rec[i]
            pl_rec[i] = temp
            s_tab.append(sol_init + bfs(graph, pl_rec))
        
        s_min = s_tab[0]
        
        for i in range(0, len(places)-2):
            #print(s_tab[i].g)
            if s_min.g > s_tab[i].g:
                s_min = s_tab[i]
        
        return s_min
    
    
import time 

#test 1  --------------  OPT. SOL. = 27
graph = read_graph()
start_time = time.time()
places=[0, 2, 7, 13, 11, 16, 15, 7, 9, 8, 4]
sol = bfs(graph=graph, places=places)
print("Solution : " + str(sol.g))
print("--- %s seconds ---" % (time.time() - start_time))
            
    
    
    
    
    

