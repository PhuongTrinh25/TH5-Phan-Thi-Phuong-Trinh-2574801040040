adj = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5), (4,8)],
    3: [(4,3), (5,6)],
    4: [(5,2)],
    5: []
}
n = 6
s = 0
t = 4
dist = [float('inf')] * n
visited = [False] * n
parent = [-1] * n
dist[s] = 0
for _ in range(n):
    u = min((i for i in range(n) if not visited[i]),
            key=lambda x: dist[x])
    visited[u] = True
    for v, w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
path = []
cur = t
while cur != -1:
    path.append(cur)
    cur = parent[cur]
path.reverse()
print("Duong di:", path)
print("Do dai:", dist[t])