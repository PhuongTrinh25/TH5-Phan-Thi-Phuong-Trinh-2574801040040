class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushBack(self, x):
        newNode = Node(x)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    def search(self, x):
        temp = self.head
        index = 0
        while temp:
            if temp.data == x:
                return index
            temp = temp.next
            index += 1
        return -1

l = LinkedList()
l.pushBack(1)
l.pushBack(2)
l.pushBack(3)
print(l.search(2))