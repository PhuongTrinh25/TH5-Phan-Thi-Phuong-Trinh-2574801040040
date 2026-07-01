class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            return ""
        return self.stack.pop()

s = Stack()
chuoi = input("Nhap chuoi: ")
for i in chuoi:
    s.push(i)
dao = ""
while len(s.stack) != 0:
    dao += s.pop()
print("Chuoi dao nguoc:", dao)