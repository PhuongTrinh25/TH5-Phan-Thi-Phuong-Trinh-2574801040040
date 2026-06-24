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
s = 0
t = 4
d1 = [float('inf')] * n
d2 = [float('inf')] * n
d1[s] = 0
pq = [(0, s)]
while pq:
    d, u = heapq.heappop(pq)
    for v, w in adj[u]:
        nd = d + w
        if nd < d1[v]:
            d2[v] = d1[v]
            d1[v] = nd
            heapq.heappush(pq, (nd, v))
        elif d1[v] < nd < d2[v]:
            d2[v] = nd
            heapq.heappush(pq, (nd, v))
print("Ngan nhat =", d1[t])
print("Ngan nhi =", d2[t])