class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)

a = ArrayList()
b = ArrayList()
a.add(1)
a.add(3)
a.add(5)
b.add(2)
b.add(4)
c = []
i = 0
j = 0
while i < len(a.arr) and j < len(b.arr):
    if a.arr[i] < b.arr[j]:
        c.append(a.arr[i])
        i += 1
    else:
        c.append(b.arr[j])
        j += 1
while i < len(a.arr):
    c.append(a.arr[i])
    i += 1
while j < len(b.arr):
    c.append(b.arr[j])
    j += 1
print(c)