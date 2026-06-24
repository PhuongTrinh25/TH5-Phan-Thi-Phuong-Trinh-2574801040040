import heapq
adj = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5), (4,8)],
    3: [(4,3), (5,6)],
    4: [(5,2)],
    5: []
}
n = 6
dist = [float('inf')] * n
dist[0] = 0
pq = [(0,0)]
while pq:
    d, u = heapq.heappop(pq)
    for v, w in adj[u]:
        nd = max(dist[u], w)
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist)