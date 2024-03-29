class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class SingleLinkedList:
    def __init__(self):
        self.head = Node(None)

    def __iter__(self):
        node = self.head.next
        while node is not None:
            yield node
            node = node.next

    def insert_node(self, data: int) -> Node:
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = Node(data)
        return current_node.next
    
    def insertNodeRecursive(self, node, data: int) -> Node:
        if node is None:
            return Node(data)
        node.next = self.insertNodeRecursive(node.next, data)
        return node
    
    def insertNodeRecursiveV2(self, node, data: int) -> Node: 
        if node.next is None:
            node.next = Node(data)
            return node.next
        return self.insertNodeRecursiveV2(node.next, data)

    def insertNodeAtPosition(self, data, position):
        node = Node(data)
        if position == 0:
            node.next = self.head
            self.head = node

def insertNodeAtHead(head, data):
    node = Node(data)
    if (head is None):
        head = node
        return head

    node.next = head
    head = node
    return head

def insertNodeAtTail(head, data):
    node = Node(data)
    if (head is None):
        head = node
        return head
    
    current_node = head
    while current_node.next is not None:
        current_node = current_node.next

    current_node.next = node
    return head

def deleteNode(head, position):
    if position < 0:
        return head
    if position == 0:
        return head.next
    current_node = head
    start_idx = 0
    while current_node.next is not None and start_idx < position:
        previous_node = current_node
        current_node = current_node.next
        start_idx += 1
    next_node = current_node.next
    previous_node.next = next_node
    return head

def insertNodeAtPosition(head, data, position):
    # node = SinglyLinkedListNode(data)
    node = Node(data)
    if position == 0:
        node.next = head
        return node
    current_node = head
    start_idx = 0
    while current_node.next is not None and start_idx < position - 1:
        current_node = current_node.next
        start_idx += 1
    print(current_node)
    node.next = current_node.next
    current_node.next = node
    return head    

from collections import deque
def reversePrint(head):
    current_node = head
    while current_node.next is not None:
        current_node = current_node.next


llist = SingleLinkedList()
llist.insert_node(16)
llist.insert_node(13)
llist.insert_node(7)
llist.insertNodeRecursive(llist.head, 10)
llist.insertNodeRecursiveV2(llist.head, 20)
for node in llist:
    print(node)