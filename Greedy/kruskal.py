def kruskals(G):
    v = len(G)
    mst = []
    visited = []
    edges = []
    for i in range(v):
        visited.append(0)
        for j in range(v):
            if G[i][j] != 0:
                edges.append((i,j,G[i][j]))
    edges.sort(key = lambda x: x[2])
    c=0
    while c<v-1:
        for edge in edges:
            if visited[edge[0]] == 0 or visited[edge[1]] == 0:
                mst.append(edge)
                visited[edge[0]] = 1
                visited[edge[1]] = 1
                c+=1
    return mst

v = int(input("No. of Vertices : "))
print("Adjacency Matrix : ")
G = [list(map(int, input().split())) for _ in range(v)]
mst = kruskals(G)
print("\nEdges\tWeight")
for x in mst:
    print(f"{x[0]+1}  {x[1]+1} \t  {x[2]}")