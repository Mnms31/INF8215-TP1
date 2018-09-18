from queue import Queue
import copy
import numpy as np
import time

def read_graph():
    return np.loadtxt("montreal", dtype='i', delimiter=',')
graph = read_graph()

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
        self.visited.append(idx)
        self.not_visited.remove(idx)
        self.g = self.g + graph[self.visited[-2],idx]

def bfs(graph, places):
    """
    Returns the best solution which spans over all attractions indicated in 'places'
    """
    S_root = Solution(places,graph)
    queue= Queue()
    Solution_finale = Solution(places,graph)
    goal = places[-1]
    best_time=1000
    print("First node: visited %s & not visited %s & score %s" %(S_root.visited,S_root.not_visited,S_root.g))
    queue.put(S_root)
    print("Goal: %s" %(goal))
    S_new=Solution(places,graph)
    print('################### START #####################')
    while list(queue.queue): #Tant que queue est pleine
        S_old=queue.get()
        #print("Dernier pris de la pile: %s" %(S_old.visited))
        S_new=copy.deepcopy(S_old)
        if S_new.not_visited == [goal]:
                S_new.add(goal)
                #Je garde si plus court path
                if (S_new.g < best_time):
                    best_time = copy.deepcopy(S_new.g)
                    Solution_finale = copy.deepcopy(S_new)
        else:
            for i in (set(places[1:-1]) & set(S_new.not_visited)):
                S_new=copy.deepcopy(S_old)
                S_new.add(i)
                queue.put(S_new)
    print("path final %s" %(Solution_finale.visited))
    print("Score final %s" %(Solution_finale.g))
    return Solution_finale
start_time = time.time()
sol=bfs(graph,[0, 5, 13, 16])
print(sol.g)
print("--- %s seconds ---" % (time.time() - start_time))
