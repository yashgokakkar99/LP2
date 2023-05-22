def kruskal(graph):
    mst=[]
    visited=[]
    visited2=set()
    edges=[]

    for node in graph.keys():
        visited.append(node)
        for to,cost in graph[node].items():
            if to not in visited:
                edges.append((cost, node, to))
    edges.sort()

    i=0
    while(i<len(graph)):
        (cost, frm ,to) = edges[i]
        if frm not in visited2 or to not in visited2:
            visited2.add(frm)
            visited2.add(to)
            mst.append((cost,frm,to))
        i+=1
    return mst

n=int(input("Enter number of vertices : "))
graph={}
for _ in range(n):
    vertex=input("Enter the vertex : ")
    edges=int(input("Enter number of edges : "))
    graph[vertex]={}
    for _ in range(edges):
        destination=input("Enter the destination vertex : ")
        cost=int(input("Enter cost : "))
        graph[vertex][destination]=cost
mst=kruskal(graph)
print(mst)