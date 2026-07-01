class Queue:
    def __init__(self):
        self.inStack = []
        self.outStack = []
    def enqueue(self, x):
        self.inStack.append(x)
    def dequeue(self):
        if len(self.outStack) == 0:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())
        if len(self.outStack) == 0:
            print("Queue rong")
        else:
            return self.outStack.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())