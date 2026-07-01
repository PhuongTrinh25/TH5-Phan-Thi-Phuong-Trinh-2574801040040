class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            return ""
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()
chuoi = input("Nhap chuoi: ")
dung = True
for i in chuoi:
    j