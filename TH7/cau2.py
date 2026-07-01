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
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
    def length(self):
        dem = 0
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            dem += 1
            temp = temp.next
        print("\nDo dai =", dem)

l = LinkedList()
l.pushBack(1)
l.pushBack(2)
l.pushBack(3)
l.length()