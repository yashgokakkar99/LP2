import heapq
def dijkstra(graph,start):
    mst=[]
    visited=set()
    heap=[(0,start)]
    while heap:
        (cost,node) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            mst.append((cost, node))
            for neighbour,new_cost in graph[node].items():
                if neighbour not in visited:
                    heapq.heappush(heap,(new_cost,neighbour))
    return mst

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
mst=dijkstra(graph,start)
print(mst)
