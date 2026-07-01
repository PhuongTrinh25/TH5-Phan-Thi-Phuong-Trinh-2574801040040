class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)

n = 5
k = 2
q = Queue()
for i in range(1, n + 1):
    q.enqueue(i)
while len(q.queue) > 1:
    for i in range(k - 1):
        q.enqueue(q.dequeue())
    print("Loai:", q.dequeue())
print("Nguoi song sot:", q.queue[0])