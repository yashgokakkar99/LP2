def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to,cost in graph[start].items()]
    edges.sort()

    while edges:
        (cost, frm, to) = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((cost, frm, to))
            for neighbour, wt in graph[to].items():
                if neighbour not in visited:
                    edges.append((cost, to, neighbour))
            edges.sort()

    return mst

g = {
    'A': {'B': 9, 'C':75},
    'B': {'A': 9, 'C': 95, 'D': 19, 'E': 42},
    'C': {'A': 75, 'B': 95, 'D': 51, 'E': 66},
    'D': {'B': 19, 'C': 51, 'E': 31},
    'E': {'B': 42, 'C': 66, 'D': 31}
}

print(prim(g,'A'))
                
