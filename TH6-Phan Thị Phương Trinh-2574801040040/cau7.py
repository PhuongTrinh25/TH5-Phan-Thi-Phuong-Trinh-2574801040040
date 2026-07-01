class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
s = Stack()
while len(q.queue) != 0:
    s.push(q.dequeue())
while len(s.stack) != 0:
    q.enqueue(s.pop())
print(q.queue)