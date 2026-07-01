class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if self.isEmpty():
            return "Queue rong"
        return self.queue.pop(0)
    def front(self):
        if self.isEmpty():
            return "Queue rong"
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.front())
print(q.isEmpty())