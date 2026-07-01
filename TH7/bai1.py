class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def get(self, index):
        if index >= 0 and index < len(self.arr):
            return self.arr[index]
        return "Vi tri khong hop le"
    def set(self, index, x):
        if index >= 0 and index < len(self.arr):
            self.arr[index] = x
    def size(self):
        return len(self.arr)

a = ArrayList()
a.add(1)
a.add(2)
a.add(3)
print(a.get(1))
print(a.size())