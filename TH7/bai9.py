class ArrayList:
    def __init__(self):
        self.arr = []
    def add(self, x):
        self.arr.append(x)
    def reverse(self):
        left = 0
        right = len(self.arr) - 1
        while left < right:
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            left += 1
            right -= 1

a = ArrayList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
print(a.arr)
a.reverse()
print(a.arr)