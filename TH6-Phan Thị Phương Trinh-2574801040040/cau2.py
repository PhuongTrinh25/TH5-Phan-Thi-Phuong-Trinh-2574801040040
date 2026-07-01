class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue day")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x
    def dequeue(self):
        if self.front == -1:
            print("Queue rong")
            return
        print("Lay ra:", self.queue[self.front])
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
