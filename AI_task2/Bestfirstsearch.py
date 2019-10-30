#Implementation of greedy best first search Algorithm using python,
#BFS is an informed graph searching algorithm its main idea is to use a heuristic function to decide
# which adjacent node is better to visit depending on the value of h(n) 

##Declaring the graph in the following 
## node: {child1:h(n),child2:h(n)}
## for the first node node 0 is connected to node 1 having h(n)=5
## and node 3 having h(n)=1 and so on for all the nodes
graph = {
    0:{1:5,2:6,3:1},  
    1:{4:6,5:5},
    2:{},
    3:{6:4,7:6},
    4:{},
    5:{},
    6:{8:10,9:0},
    7:{}
    }
nodes_conn = [
     [1,2,3],
     [4,5],
     [],
     [6,7],
     [],
     [],
     [8,9],
     []]   

visited=[]
nxt_node=0 ##which node to visit next
min_k=0    ##the key of the minimum cost of the child of the current node
cost= 0    ##the cost of the node
#print(min_k)
def best_first_search (start,goal):
    visited.append(start)
    if start==goal:
        print('success')
        return visited
    if len(visited)==0:
        print("failed")
        exit
    else:
        min_k= min(graph[start],key=graph[start].get)        
        nxt_node = min_k  
        cost= graph[start][min_k]
        print("Next Node >>" , nxt_node , "Heuristic = ",cost)
        best_first_search(nxt_node,goal) 
    return visited
    
res=[]
res=best_first_search(0,9)
print(res)







