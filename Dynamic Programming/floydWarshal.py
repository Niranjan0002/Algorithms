INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)

    dist = [row[:] for row in graph] 

    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = [
    [0,4,INF,5,INF],
    [INF,0,1,INF,6],
    [2,INF,0,3,INF],
    [INF,INF,1,0,2],
    [1,INF,INF,4,0]
]

# Number of vertices
V = len(graph)
print("-----ADJACENCY MATRIX-----")
for i in range(V):
    for j in range(V):
        if graph[i][j] == INF:
            print('INF', end='\t')
        else:
            print(graph[i][j], end='\t')
    print()

result = floyd_warshall(graph)

print("\n\n-----SHORTEST PATH MATRIX-----")
for i in range(V):
    for j in range(V):
        if result[i][j] == INF:
            print('INF', end='\t')
        else:
            print(result[i][j], end='\t')
    print()

