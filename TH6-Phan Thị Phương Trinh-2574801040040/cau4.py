class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
    def enqueue(self, x):
        if len(self.queue) == self.size:
            print("Queue day")
        else:
            self.queue.append(x)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue rong")
        else:
            print("Lay ra:", self.queue.pop(0))
    def count(self):
        return len(self.queue)

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("So phan tu:", q.count())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()