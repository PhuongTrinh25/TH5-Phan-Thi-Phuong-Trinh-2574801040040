import heapq
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
n = len(grid)
m = len(grid[0])
dist = [[float('inf')] * m for _ in range(n)]
dist[0][0] = grid[0][0]
pq = [(grid[0][0], 0, 0)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while pq:
    d, x, y = heapq.heappop(pq)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            nd = d + grid[nx][ny]
            if nd < dist[nx][ny]:
                dist[nx][ny] = nd
                heapq.heappush(pq, (nd, nx, ny))
print(dist[n-1][m-1])