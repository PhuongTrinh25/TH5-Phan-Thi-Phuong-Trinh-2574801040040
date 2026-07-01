class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def removeDuplicate(self):
        newArr = []
        for i in self.arr:
            if i not in newArr:
                newArr.append(i)
        self.arr = newArr

a = ArrayList()
a.add(3)
a.add(1)
a.add(3)
a.add(2)
a.add(1)
print(a.arr)
a.removeDuplicate()
print(a.arr)