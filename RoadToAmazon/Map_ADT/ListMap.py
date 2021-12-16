from IMap import IMap

# Ordered List


class ListMap(IMap):
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.value = v
            self.next = None

        def __repr__(self):
            return '(' + self.key + ',' + self.value + ')'

    def __init__(self):
        self.head = None
        self.NEntries = 0

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def lookupNode(self, k: str) -> Node:
        for e in self:
            if e.key == k:
                return e

    def size(self):
        return self.NEntries

    def isEmpty(self):
        return self.NEntries == 0

    def put(self, k, v):
        e = self.lookupNode(k)
        if e is not None:
            e.value = v
            return

        e = self.Node(k, v)
        if self.head is None:
            self.head = e
        elif k < self.head.key:
            e.next = self.head
            self.head = e
        else:
            ptr1 = self.head
            ptr2 = self.head.next
            while ptr2 is not None:
                if ptr2.key > k:
                    break
                ptr1 = ptr2
                ptr2 = ptr2.next
            ptr1.next = e
            e.next = ptr2
        self.NEntries += 1

    def get(self, k):
        e = self.lookupNode(k)
        if e is not None:
            return e.value
        else:
            return None

    def remove(self, k):
        ptr1 = self.head
        ptr2 = self.head.next
        while ptr2 is not None:
            if ptr2.key == k:
                break
            ptr1 = ptr2
            ptr2 = ptr2.next
        if ptr2:
            ptr1.next = ptr2.next
            self.NEntries -= 1
        return k


list_map = ListMap()
# list_map.put(1,'a')
# list_map.put(2, 'b')
# list_map.put(3, 'c')
# list_map.put(2, 'd')

list_map.put('man', 'male person')
list_map.put('woman', 'female person')
list_map.put('pen', 'writing instrument')
list_map.put('man', 'guy')

print(list_map.get('man'))