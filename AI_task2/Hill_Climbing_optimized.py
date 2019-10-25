# hill climbing is a heuristic search algorithm

# A simple hill climbing algorithm will do the following
#     1- Define the current state as an initial state
#     2- Loop until the goal state is achieved or no more operators can be applied on the current state:
#           2.1 Apply an operation to current state and get a new state
#           2.2 Compare the new state with the goal
#           2.3 Quit if the goalstate is achieved
#           2.4 Evaluate new state with heuristic function and compare it with the current state
#           2.5 If the newer state is closer to the goal compared to current state, update the current state

# Simple as it seems hill climbing algorithm suffers from local maximum problem where
# All its next states are no better than the current state so it's reached the local maximum
# while there is another better maximum somewhere else but it doesn't know about since it's 
# greedly checking for the best current choice

# As a solution to this problem backtrack is utilized to overcome the local maximum
# problem by string the previous state.

from array import *

# Let's assume a problem where we start from node 0 and our goal is to reach node g

Dict_connections = {0: {2:3 , 1:5 } ,   #an edge between 0,2 costs: 3 & edge between 0,1 costs: 5
                    1: {3:2 , 4:9 } ,   #an edge between 1,3 costs: 2 & edge between 1,4 costs: 9
                    2: {5:7 , 6:90} }   #an edge between 2,5 costs: 7 & edge between 2,6 costs: 90

nodes = [[2 , 1] ,      # Node 0 connected to 1 , 2  sorted by cost
         [3 , 4] ,      # Node 1 connected to 3 , 4  sorted by cost  
         [5 , 6] ,      # Node 2 connected to 5 , 6  sorted by cost
         [],            # Node 3 connected to nothing
         [],            # Node 4 connected to nothing
         [],            # Node 5 connected to nothing
         []]            # Node 6 connected to nothing


def hillWithBacktrack(i , goal) :
    if i == goal:
        return goal
    cost = 99
    ret  = 99
    next_node = 0
    # nodes are sorte by cost so try each node trying to find goal
    for j in range (len(nodes[i])): 
            cost = Dict_connections[i][nodes[i][j]]
            next_node = nodes[i][j]
            print("next: ",next_node ," Cost: ", cost)        
            ret = hillWithBacktrack(next_node , goal)
            if ret == goal:
                break
    return ret


g = 4
ret = hillWithBacktrack(0 , g)
if ret == g:
    print("Goal found")
else :
    print("reached end of tree with no goal")

