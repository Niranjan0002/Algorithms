def safetyCheck(v, graph, colour, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and colour[i] == c:
            return False
    return True

def colour_util(graph, m, colour, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if safetyCheck(v, graph, colour, c):
            colour[v] = c
            if colour_util(graph, m, colour, v + 1):
                return True
            colour[v] = 0

def colouring(graph, m):
    num_vertices = len(graph)
    colour = [0] * num_vertices
    if not colour_util(graph, m, colour, 0):
        print("No solution exists.")
        return False
    print("Solution exist and Following are the assigned colours:")
    for c in colour:
        print(c, end=' ')
    return True

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]]
m = 3
colouring(graph, m)
