class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
    def push(self, x):
        if len(self.stack) == self.size:
            print("Overflow")
        else:
            self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            print("Underflow")
        else:
            print("Lay ra:", self.stack.pop())

s = Stack(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.pop()
s.pop()
s.pop()