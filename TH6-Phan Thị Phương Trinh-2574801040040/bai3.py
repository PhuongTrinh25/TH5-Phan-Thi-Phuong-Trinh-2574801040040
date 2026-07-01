class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack rong")
        else:
            print("Pop:", self.stack.pop())

s = Stack()
s.push(5)
s.push(7)
s.pop()
print("Stack cuoi cung:", s.stack)