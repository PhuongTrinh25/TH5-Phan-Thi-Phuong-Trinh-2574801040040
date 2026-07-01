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
    def insertAfter(self, value, x):
        temp = self.head
        while temp:
            if temp.data == value:
                newNode = Node(x)
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

l = LinkedList()
l.pushBack(1)
l.pushBack(3)
l.insertAfter(1, 2)
l.printList()