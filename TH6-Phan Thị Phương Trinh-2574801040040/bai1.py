class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if self.isEmpty():
            return "Stack rong"
        return self.stack.pop()
    def top(self):
        if self.isEmpty():
            return "Stack rong"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())    
print(s.top())    
print(s.isEmpty())