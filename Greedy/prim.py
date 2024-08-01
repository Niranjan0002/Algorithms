def minOut(G, visited):
    min_edge = None
    for i in visited:
        for j in range(len(G)):
            if j not in visited and G[i][j] != 0:
                if min_edge is None or G[i][j] < min_edge[2]:
                    min_edge = (i, j, G[i][j])
    return min_edge

def prims(G):
    mst = []
    visited = [0] 
    while len(visited) < len(G):
        min_edge = minOut(G, visited)
        mst.append(min_edge)
        visited.append(min_edge[1])
    return mst

v = int(input("No. of Vertices : "))
print("Adjacency Matrix : ")
G = [list(map(int, input().split())) for _ in range(v)]
mst = prims(G)
print("\nEdges\tWeight")
for edge in mst:
    print(f"{edge[0] + 1}  {edge[1] + 1} \t  {edge[2]}")