class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
    def add(self, x):
        if self.size == self.capacity:
            self.capacity *= 2
            newArr = [None] * self.capacity
            for i in range(self.size):
                newArr[i] = self.arr[i]
            self.arr = newArr
        self.arr[self.size] = x
        self.size += 1
    def printList(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()

a = ArrayList()
for i in range(1, 7):
    a.add(i)
print("Capacity =", a.capacity)
a.printList()