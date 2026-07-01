class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue) == 0

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}
visited = []
q = Queue()
start = 0
q.enqueue(start)
print("BFS:")
while not q.isEmpty():
    node = q.dequeue()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for i in graph[node]:
            q.enqueue(i)