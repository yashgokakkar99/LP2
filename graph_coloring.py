def print_configuration(color_array):
    for i,color in enumerate(color_array):
        print("Vertex => ",i,"Color => ",color)
    return True

def issafe(graph, vertex, color_array, color):
    for i in range(len(graph)):
        if graph[vertex][i] and color_array[i]==color:
            return False
    return True

def algorithm(graph, vertex, color_array, m):
    if vertex==len(graph):
        print_configuration(color_array)
        return True
    for color in range(1,m+1):
        if issafe(graph, vertex, color_array, color):
            color_array[vertex]=color
            if algorithm(graph, vertex+1, color_array, m):
                return True
        color_array[vertex]=0
    return False

if __name__ == '__main__':
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []

    print("Enter the adjacency matrix (1 for edge, 0 for no edge): ")
    for i in range(num_vertices):
        row = list(map(int, input().split()))
        graph.append(row)

    m=int(input("Enter m : "))
    vertex=int(input("Enter vertex : "))
    color_array = [0]*len(graph)
    if(algorithm(graph,vertex,color_array,m)):
        print("Coloring is possible !!")
    else:
        print("Fuck hard next time babes !!")
