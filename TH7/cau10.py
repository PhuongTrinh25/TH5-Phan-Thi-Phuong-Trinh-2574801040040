class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def deleteK(head, k):
    fast = head
    slow = head
    for i in range(k):
        fast = fast.next
    if fast == None:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = deleteK(head, 2)
printList(head)