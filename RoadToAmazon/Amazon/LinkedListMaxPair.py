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

    def print_nodes(self):
        for x in self:
            print(x)


def find_max_of_first_last(head):
    pass


ll = SingleLinkedList()
ll.insert_node(1)
ll.insert_node(4)
ll.insert_node(3)
ll.insert_node(2)
ll.print_nodes()


def passwordStrength(password):
    last = {chr(97 + i): -1 for i in range(26)}
    ret = 0
    for i, ch in enumerate(password):
        left = i - last[ch]
        right = len(password) - i
        ret += left * right
        last[ch] = i

    return ret

print(passwordStrength('good'))