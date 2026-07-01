class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()

s = Stack()
bieu_thuc = input("Nhap bieu thuc: ")
ds = bieu_thuc.split()
for x in ds:
    if x.isdigit():
        s.push(int(x))
    else:
        b = s.pop()
        a = s.pop()
        if x == "+":
            s.push(a + b)
        elif x == "-":
            s.push(a - b)
        elif x == "*":
            s.push(a * b)
        elif x == "/":
            s.push(a / b)
print("Ket qua =", s.pop())