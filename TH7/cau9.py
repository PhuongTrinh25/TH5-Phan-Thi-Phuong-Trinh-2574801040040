class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def merge(a, b):
    if a == None:
        return b
    if b == None:
        return a
    if a.data < b.data:
        head = a
        head.next = merge(a.next, b)
    else:
        head = b
        head.next = merge(a, b.next)
    return head
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

a = Node(1)
a.next = Node(3)
a.next.next = Node(5)
b = Node(2)
b.next = Node(4)
head = merge(a, b)
printList(head)