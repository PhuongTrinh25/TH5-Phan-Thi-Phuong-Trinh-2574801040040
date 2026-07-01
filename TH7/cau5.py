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
    def delete(self, x):
        if self.head.data == x:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == x:
                temp.next = temp.next.next
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
l.pushBack(2)
l.pushBack(3)
l.pushBack(2)
l.delete(2)
l.printList()