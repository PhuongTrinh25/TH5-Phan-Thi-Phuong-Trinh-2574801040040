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
    def middle(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print("Nut giua =", slow.data)

l = LinkedList()
l.pushBack(1)
l.pushBack(2)
l.pushBack(3)
l.pushBack(4)
l.pushBack(5)
l.middle()