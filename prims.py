def prims(graph, start):
    mst=[]
    visited=set([start])
    edges=[(cost,start,to) for to,cost in graph[start].items()]
    edges.sort()
    while edges:
        (cost,frm,to) = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((cost,frm,to))
            for neighbour,cost in graph[to].items():
                if neighbour not in visited:
                    edges.append((cost, to, neighbour))
            edges.sort()
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
mst = prims(graph,start)
print(mst)
