class Deque:
    def __init__(self):
        self.data = []
    def pushFront(self, x):
        self.data.insert(0, x)
    def pushBack(self, x):
        self.data.append(x)
    def popFront(self):
        if len(self.data) == 0:
            print("Deque rong")
        else:
            return self.data.pop(0)
    def popBack(self):
        if len(self.data) == 0:
            print("Deque rong")
        else:
            return self.data.pop()
    def isEmpty(self):
        return len(self.data) == 0

d = Deque()
d.pushFront(1)
d.pushBack(2)
d.pushFront(3)
print(d.data)
print("Pop Front:", d.popFront())
print("Pop Back:", d.popBack())
print(d.data)