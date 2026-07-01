class ArrayList:
    def __init__(self):
        self.arr = []
    def append(self, x):
        self.arr.append(x)
    def popBack(self):
        if len(self.arr) == 0:
            print("Danh sach rong")
        else:
            return self.arr.pop()

a = ArrayList()
a.append(1)
a.append(2)
a.append(3)
print(a.popBack())
print(a.arr)