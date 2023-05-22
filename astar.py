import heapq
def astar(graph,start,heuristic,goal):
    mst=[]
    visited=set()
    heap=[(0,start)]
    while heap:
        (cost,node) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            mst.append((cost, node))
            if node==goal:
                break
            for neighbour,new_cost in graph[node].items():
                if neighbour not in visited:
                    priority = cost+new_cost+heuristic(neighbour)
                    heapq.heappush(heap,(priority,neighbour))
    return mst

def heuristic_function(node):
    # Define the heuristic cost for each node based on domain knowledge
    # You can predefine the heuristic values or use a different approach
    # For simplicity, let's assume the heuristic values are already defined
    heuristic_values = {
        'A': 10,
        'B': 5,
        'C': 8,
        'D': 3,
        'E': 0,
    }
    return heuristic_values[node]

n=int(input("Enter number of vertices : "))
graph={}
for _ in range(n):
    vertex=input("Enter the vertex : ")
    edges=int(input("Enter the number of edges : "))
    graph[vertex]={}
    for _ in range(edges):
        destination=input("Enter the destination vertex : ")
        cost=int(input("Enter the cost : "))
        graph[vertex][destination]=cost
start=input("Enter start vertex : ")
goal=input("Enter goal vertex : ")
mst=astar(graph,start,heuristic_function,goal)
print(mst)
