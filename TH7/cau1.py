class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushFront(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode
    def pushBack(self, x):
        newNode = Node(x)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

l = LinkedList()
l.pushFront(2)
l.pushBack(5)
l.printList()