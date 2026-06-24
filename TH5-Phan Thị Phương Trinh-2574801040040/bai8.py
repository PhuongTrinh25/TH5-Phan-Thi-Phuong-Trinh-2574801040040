adj = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5), (4,8)],
    3: [(4,3), (5,6)],
    4: [(5,2)],
    5: []
}
D = 3
n = 6
dist = [float('inf')] * n
visited = [False] * n
dist[0] = 0
for _ in range(n):
    u = min((i for i in range(n) if not visited[i]),
            key=lambda x: dist[x])
    visited[u] = True
    for v, w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
count = 0
for d in dist:
    if d <= D:
        count += 1
print("So dinh =", count)