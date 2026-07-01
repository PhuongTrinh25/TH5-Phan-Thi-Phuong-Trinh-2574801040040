class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def indexOf(self, x):
        for i in range(len(self.arr)):
            if self.arr[i] == x:
                return i
        return -1

a = ArrayList()
a.add(5)
a.add(3)
a.add(7)
print(a.indexOf(7))