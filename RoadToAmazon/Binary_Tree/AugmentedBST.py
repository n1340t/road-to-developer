from collections import deque
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.lCount = 0
  def __repr__(self):
    return str(str(self.key) + ' lCount: ' + str(self.lCount))

class BST:
  def __init__(self):
    self.root = None

  def insert(self, node, key):
    if node is None:
      return Node(key)
    if node.key > key:
      node.left = self.insert(node.left, key)
      node.lCount += 1
    elif node.key < key:
      node.right = self.insert(node.right, key)
    return node

  # Complexity is O(logN), in-order
  def unrank(self, node, k):
    # print(node, k)
    if k == node.lCount + 1:
      return node
    elif k < node.lCount + 1:
      return self.unrank(node.left, k)
    else:
      return self.unrank(node.right, k - node.lCount - 1) # subtract right node itself
  # select = unrank, complexity is O(n), in-order
  def select(self, root, k):
    # Base case
    if (root == None):
        return None
    count = root.lCount + 1
    if (count == k):
        return root
    if (count > k):
        return self.select(root.left, k)
    # Else search in right subtree
    return self.select(root.right, k - count)

  # Complexity is O(n), in-order
  def select_with_stack(self, root, k):
    stack = deque(maxlen=k)
    while True:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      k -= 1
      if k == 0:
        return root
      # root can be None and placing root = stack.pop() here still break the code because of line 59
      root = root.right

  def inOrder(self, root):
    if root is None:
      return
    self.inOrder(root.left)
    print(root, root.lCount)
    return self.inOrder(root.right)

if __name__ == '__main__':
  tree = BST()
  tree.root = tree.insert(tree.root, 20)
  tree.insert(tree.root, 8)
  tree.insert(tree.root, 22)
  tree.insert(tree.root, 4)
  tree.insert(tree.root, 12)
  tree.insert(tree.root, 10)
  tree.insert(tree.root, 14)
  # tree.inOrder(tree.root)
  for x in range(1,2):
    print('Testing...', x)
    # print(tree.select(tree.root, x))
    print(tree.select_with_stack(tree.root, x))
    print(tree.select_with_monotonic_stack(tree.root, x))
    # print(tree.unrank(tree.root, x))