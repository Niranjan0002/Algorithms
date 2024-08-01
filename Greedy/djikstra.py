def minDistance(dist,visited):
    mindist = 100000
    v = len(dist)
    for ver in range(v):
        if visited[ver] == 0 and dist[ver]<mindist:
            mindist = dist[ver]
            minv = ver
    return minv

def dijkstra(S, G):
    v = len(G)
    visited = [0] * v
    dist = [100000] * v
    dist[S] = 0
    for i in range(v):
        u = minDistance(dist,visited)
        visited[u] = 1
        for ver in range(v):
            if visited[ver] == 0 and G[u][ver]!=0 and G[u][ver] + dist[u] < dist[ver]:
                dist[ver] = G[u][ver] + dist[u]
    return dist

v = int(input("No. of Vertices : "))
print("Adjacency Matrix : ")
G = [list(map(int,input().split())) for i in range(v)]
S = int(input("\nSource : ")) - 1
dist = dijkstra(S,G)
print()
for i in range(v):
    print(f"vertex {S+1} to vertex {i+1} = {dist[i]}")