class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def removeEven(self):
        newArr = []
        for i in self.arr:
            if i % 2 != 0:
                newArr.append(i)
        self.arr = newArr

a = ArrayList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
print(a.arr)
a.removeEven()
print(a.arr)