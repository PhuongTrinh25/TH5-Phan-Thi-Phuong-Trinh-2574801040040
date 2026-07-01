class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue rong")
        else:
            print("Dequeue:", self.queue.pop(0))

q = Queue()
q.enqueue(5)
q.enqueue(7)
q.dequeue()
print("Queue cuoi cung:", q.queue)