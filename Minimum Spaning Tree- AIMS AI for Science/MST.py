from heapq import heappop,heappush
from modules import UF
n=7
mapper={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}

input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''
graph=[[(10,2),(14,1),(19,2)],                      #A
       [(14,0),(15,3),(18,4)],                      #B
       [(10,0),(26,3),(29,5)],                      #C
       [(19,0),(15,1),(26,2),(16,4),(21,6),(17,5)], #D
       [(18,1),(16,3),(9,6)],                       #E
       [(29,2),(17,3),(25,6)],                      #F
       [(9,4),(21,3),(25,5)]]                       #G

def parse_input_to_adj_list(input_network):
    lines = input_network.strip().split('\n')
    n = len(lines)  # Number of vertices
    adj_list = [[] for _ in range(n)]  # Initialize adjacency list
    
    for i, line in enumerate(lines):
        weights = line.split(',')
        for j, weight in enumerate(weights):
            if weight.isdigit():  # Check if there's a valid edge
                adj_list[i].append((int(weight), j))  # Add edge with weight and destination vertex index
                
    return adj_list

graph = parse_input_to_adj_list(input_network)

# for i, edges in enumerate(adj_list):
#     print(f"Vertex {i}: {edges}")
print(adj_list)

edges_in_mst=[]
total_cost = 0
edges_list_sorted = []


















# for i in range(len(graph)):
#     for j in graph[i]:
#         heappush(edges_list_sorted,(j[0],i,j[1]))
# union_find = UF(n)
# for i in range(len(edges_list_sorted)):
#     edge = heappop(edges_list_sorted)
#     w,u,v = edge[0],edge[1],edge[2]
#     if union_find.find(u)!= union_find.find(v):
#         edges_in_mst.append(edge)
#         total_cost+= w
#         union_find.union(u,v)
# print(f"the list of Edges in mst :{edges_in_mst}","\n",f"The total cost is: {total_cost}")
# print(edges_list_sorted)






