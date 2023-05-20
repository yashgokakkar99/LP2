import heapq
def dij(graph, start):
    mst=[]
    visited=set()
    heap = [(0,start)] #(cost, node)
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            mst.append((cost, node))

            for neighbour, weight in graph[node].items():
                if neighbour not in visited:
                    heapq.heappush(heap,(weight, neighbour))
    return mst
graph = {
    'A': {'B': 9, 'C':75},
    'B': {'A': 9, 'C': 95, 'D': 19, 'E': 42},
    'C': {'A': 75, 'B': 95, 'D': 51, 'E': 66},
    'D': {'B': 19, 'C': 51, 'E': 31},
    'E': {'B': 42, 'C': 66, 'D': 31}
}
mst = dij(graph,'A')
print(mst)
