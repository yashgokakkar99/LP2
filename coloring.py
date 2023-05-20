def print_configuration(color_array):
    print("The assigned colors are as follows:")
    for i, color in enumerate(color_array):
        print("Vertex:", i, "Color:", color)


def is_safe(graph, vertex ,color_array ,color):
    for i in range(len(graph)):
        if graph[vertex][i] and color_array[i] == color:
            return False
    return True


def graph_coloring_algorithm(graph,vertex, color_array, m):
    if vertex == len(graph):
        print_configuration(color_array)
        return True

    for color in range(1, m + 1):
        if is_safe(graph, vertex,color_array, color):
            color_array[vertex] = color
            if graph_coloring_algorithm(graph,  vertex + 1, color_array, m):
                return True
            color_array[vertex] = 0

    return False


if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3
    color_array = [0] * len(graph)

    if graph_coloring_algorithm(graph, 0, color_array, m):
        print("Coloring is possible!")
    else:
        print("Coloring is not possible!")
