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
count = [0] * n
dist[0] = 0
count[0] = 1
pq = [(0, 0)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        nd = dist[u] + w
        if nd < dist[v]:
            dist[v] = nd
            count[v] = count[u]
            heapq.heappush(pq, (nd, v))
        elif nd == dist[v]:
            count[v] += count[u]

print("dist =", dist)
print("count =", count)