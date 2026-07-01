class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    def push(self, x):
        self.q1.append(x)
    def pop(self):
        if len(self.q1) == 0:
            print("Stack rong")
            return
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        print("Pop:", self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
print(s.q1)