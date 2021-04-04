class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_node(self, data: int):
        node = Node(data)
        if (self.head is None):
            self.head = node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = node

def reversePrint(head):
  if (head is None or head.next is None):
    return head
  
  current_node = head.next 

  reversed_node = head
  reversed_node.next = None

  while current_node is not None:
    temp = current_node
    current_node = current_node.next

    temp.next = reversed_node
    reversed_node = temp

  return reversed_node

def reversePrintV2(head):
  if head is None or head.next is None:
    return head
  reversed_node = reversePrintV2(head.next)
  head.next.next = head
  head.next = None
  return reversed_node

llist = SingleLinkedList()

llist.insert_node(10)
llist.insert_node(20)
llist.insert_node(30)
llist.insert_node(40)
llist.insert_node(50)

new_head = reversePrintV2(llist.head)

while new_head is not None:
  print(new_head)
  new_head = new_head.next