adj = {
    'A': [('B',5), ('C',3)],
    'B': [('A',5), ('C',1), ('D',2)],
    'C': [('A',3), ('B',1), ('D',6)],
    'D': [('B',2), ('C',6), ('E',4)],
    'E': [('D',4)]
}
dist = {v: float('inf') for v in adj}
visited = {v: False for v in adj}
dist['A'] = 0
for _ in range(len(adj)):
    u = min((v for v in adj if not visited[v]),
            key=lambda x: dist[x])
    visited[u] = True
    for v, w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
print(dist)