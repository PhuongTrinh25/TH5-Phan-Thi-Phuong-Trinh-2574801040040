class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def rotate(self, k):
        n = len(self.arr)
        k = k % n
        self.arr = self.arr[n-k:] + self.arr[:n-k]

a = ArrayList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
print(a.arr)
a.rotate(2)
print(a.arr)