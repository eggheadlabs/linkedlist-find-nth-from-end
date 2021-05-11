# How do you find the n'th node from the end in a singly linked list?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def nth_from_end(self, n):
        ptr = self.head
        ptr_ref = self.head     # reference pointer
        # move ptr n steps ahead
        for _ in range(n):
            ptr = ptr.next
        # then move both pointers towards to the end. the last ptr_ref is the nth node from the end
        while ptr:
            ptr = ptr.next
            ptr_ref = ptr_ref.next
        return ptr_ref

# Preparation: create the SinglyLinkedList according to a given data
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s.reverse()
sll = SinglyLinkedList()
for x in s: sll.push(x)

# find the n'th node from the end 
if sll.head is not None:
    node = sll.nth_from_end(3)
    print('Found the n\'th element from the end: ', node.data)
