from queue import Queue
import copy
import numpy as np
import time
import heapq


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
        self.h = 0
        self.g = 0  # current cost
        self.f = 0
        self.graph = graph
        self.visited = [places[0]]  # list of already visited attractions
        self.not_visited = copy.deepcopy(places[1:])  # list of attractions not yet visited

    def add(self, idx):
        """
        Adds the point in position idx of not_visited list to the solution
        """
        self.visited.append(idx)
        self.not_visited.remove(idx)
        self.g = self.g + graph[self.visited[-2], idx]

    def __𝚕𝚝__(self, other):
        self.f=self.h +self.g
        other.f = other.h + other.g
        if self.f < other.f:
            return True
        else:
            return False



def fastest_path_estimation(sol):
    """
    Returns the time spent on the fastest path between
    the current vertex c and the ending vertex pm
    """
    start_time = time.time()
    SOL=copy.deepcopy(sol)
    SOL.h = 0
    c = SOL.visited[-1]
    pm = SOL.not_visited[-1]
    place = SOL.not_visited
    # print("place: %s" %(place))
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0,[c]))
    explored = 0 #opde explored
    while queue:
        # for i in queue:
        #     print("Elelements de ma liste: %s " %(list(i)))
        # print("+++++++++++++++++++++++++++++++++++++++++++")
        S_Old = heapq.heappop(queue) #dernier element de la liste
        neighbours = list(set(place) - set(S_Old[1]))
        visited=list(S_Old[1])
        explored += 1
        if  pm in visited: #si derniere element est une solution complete c est donc la plus courte (decommenter plus haut pour le voir)
            print("--- %s seconds ---" % (time.time() - start_time))
            return S_Old[0]

        if neighbours == [pm]:
            cost = S_Old[0]
            cost += graph[visited[-1], pm]
            S_Old[1].append(pm)            # print("# of nodes explored: %s" % (explored))
            heapq.heappush(queue,(cost,S_Old[1]))
        else:
            for i in neighbours[:-1]:
                S_New = copy.deepcopy(S_Old)
                cost = S_New[0]
                cost += graph[visited[-1],i]
                S_New[1].append(i)
                heapq.heappush(queue,(cost,S_New[1]))

#TEST DJIKSTRA
# start_time = time.time()
# places=[0,1,2,3,4]
# TEST=Solution(graph=graph,places=places)
# TEST.visited=[0]
# TEST.not_visited=[1,2,3,4]
# sol=fastest_path_estimation(TEST)
# print(sol)
# print("--- %s seconds ---" % (time.time() - start_time))



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
    goal = places[-1]
    explore=0
    while T:
        S_old = heapq.heappop(T)
        explore += 1
        print(S_old.visited)
        if S_old.not_visited == [goal]:
            S_old.add(goal)
            print("# of nodes explored: %s" % (explore))
            return S_old
        else:
            for i in S_old.not_visited[:-1]: #pour tout i dans les element non visites (restants)
                S_new = copy.deepcopy(S_old)
                S_new.h=0
                S_new.add(i)
                S_new.h= fastest_path_estimation(S_new)
                print(S_new.visited)
                heapq.heappush(T, S_new) #ajout a  la liste et ordonnner

##test 1  --------------  OPT. SOL. = 27
# start_time = time.time()
# places=[0, 5, 13, 16, 6, 9, 4]
# astar_sol = A_star(graph=graph, places=places)
# print(astar_sol.g)
# print(astar_sol.visited)
# print("--- %s seconds ---" % (time.time() - start_time))

# test 2  --------------  OPT. SOL. = 30
# start_time = time.time()
# places=[0, 1, 4, 9, 20, 18, 16, 5, 13, 19]
# astar_sol = A_star(graph=graph, places=places)
# print(astar_sol.g)
# print(astar_sol.visited)
# print("--- %s seconds ---" % (time.time() - start_time))

#
#test 3  --------------  OPT. SOL. = 26
# start_time = time.time()
# places=[0, 2, 7, 13, 11, 16, 15, 7, 9, 8, 4]
# astar_sol = A_star(graph=graph, places=places)
# print(astar_sol.g)
# print(astar_sol.visited)
# print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
places = [0, 2, 20, 3, 18, 12, 13, 5, 11, 16, 15, 4, 9, 14, 1]
sol = A_star(graph=graph, places=places)
print(sol.g)
print("--- %s seconds ---" % (time.time() - start_time))


