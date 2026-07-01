class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            return
        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()
    def getMin(self):
        if len(self.minStack) == 0:
            return None
        return self.minStack[-1]

s = MinStack()
s.push(5)
s.push(3)
s.push(7)
print("Min =", s.getMin())
s.pop()
print("Min =", s.getMin())