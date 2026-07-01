class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def printList(self):
        dem = 0
        for i in self.arr:
            print(i, end=" ")
            if i % 2 == 0:
                dem += 1
        print("\nSo phan tu chan =", dem)

a = ArrayList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.printList()