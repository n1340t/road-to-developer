from collections import deque

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
  def __repr__(self):
    return str(self.key)

class BST:
  def __init__(self):
    self.root = None

  def insert(self, root, key):
    if root is None: return Node(key)
    if key < root.key:
      root.left = self.insert(root.left, key)
    elif key > root.key:
      root.right = self.insert(root.right, key)
    return root

  def inOrder(self, root):
    if root is not None:
      self.inOrder(root.left)
      print(root)
      self.inOrder(root.right)

  def preOrder(self, root):
    if root is not None:
      print(root)
      self.preOrder(root.left)
      self.preOrder(root.right)

  def postOrder(self, root):
    if root is not None:
      self.postOrder(root.left)
      self.postOrder(root.right)
      print(root)

  def levelOrder(self, root):
    queue = deque()
    queue.append(root)
    while queue:
      node = queue.popleft()
      if node:
        print(node)
        queue.append(node.left)
        queue.append(node.right)

tree = BST()
tree.root = tree.insert(tree.root, 5)
tree.insert(tree.root, 3)
tree.insert(tree.root, 7)
tree.insert(tree.root, 2)
tree.insert(tree.root, 1)
tree.insert(tree.root, 4)
tree.insert(tree.root, 6)
tree.insert(tree.root, 8)

tree.postOrder(tree.root)