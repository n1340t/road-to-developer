# lamgiang01070108@gmail.com

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def addEnd(self, node: Node):
        if (self.tail == None):
            self.tail = node
            node.next = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
    def addFromList(self, _list: list):
        for item in _list:
            self.addEnd(Node(item))

    def createlistWithLeftRotation(self, rotations):
        rotatedList = []
        head = self.tail.next
        for _ in range(rotations):
            head = head.next
    
        rotatedList.append(head.data)
        temp = head.next
        while temp != head:
            rotatedList.append(temp.data)
            temp = temp.next
        return rotatedList

clist = CircularLinkedList()
clist.addFromList([0,2,0,4,5])

res = clist.createlistWithLeftRotation(4)
for x in res:
    print(x)