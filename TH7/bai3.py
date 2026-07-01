class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def insert(self, index, x):
        self.arr.insert(index, x)
    def remove(self, index):
        if index >= 0 and index < len(self.arr):
            self.arr.pop(index)

a = ArrayList()
a.add(1)
a.add(2)
a.add(4)
a.insert(2, 3)
print(a.arr)
a.remove(1)
print(a.arr)