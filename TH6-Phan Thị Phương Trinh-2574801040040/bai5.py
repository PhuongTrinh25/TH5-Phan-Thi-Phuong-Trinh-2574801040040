class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
phu = Stack()
dem = 0
print("Thu tu LIFO:")
while len(s.stack) != 0:
    x = s.pop()
    print(x)
    phu.push(x)
    dem += 1
while len(phu.stack) != 0:
    s.push(phu.pop())
print("So phan tu:", dem)
print("Stack sau khi khoi phuc:", s.stack)