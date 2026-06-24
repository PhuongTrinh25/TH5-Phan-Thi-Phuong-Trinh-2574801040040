import heapq
adj = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
cost = [2, 3, 1, 4]
n = 4
dist = [float('inf')] * n
dist[0] = cost[0]
pq = [(dist[0], 0)]
while pq:
    d, u = heapq.heappop(pq)
    for v in adj[u]:
        nd = dist[u] + cost[v]
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))
print(dist)