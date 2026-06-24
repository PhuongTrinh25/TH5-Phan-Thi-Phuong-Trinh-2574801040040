import heapq
adj = {
    0: [(1,0.8), (2,0.5)],
    1: [(2,0.9)],
    2: []
}
prob = [0] * 3
prob[0] = 1
pq = [(-1,0)]
while pq:
    p, u = heapq.heappop(pq)
    p = -p
    for v, w in adj[u]:
        np = p * w
        if np > prob[v]:
            prob[v] = np
            heapq.heappush(pq, (-np, v))

print(prob)