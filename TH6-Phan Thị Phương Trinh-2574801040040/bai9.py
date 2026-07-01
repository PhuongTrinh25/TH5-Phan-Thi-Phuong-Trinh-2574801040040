class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
def muc(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2
    return 0

s = Stack()
infix = input("Nhap bieu thuc: ")
