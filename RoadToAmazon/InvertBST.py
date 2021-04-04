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

  def insert(self, node, key):
    if node is None: return Node(key)
    if key < node.key:
      node.left = self.insert(node.left, key)
    elif key > node.key:
      node.right = self.insert(node.right, key)
    return node
    
  def inOrder(self, root):
    if root is not None:
        self.inOrder(root.left)
        print(root)
        self.inOrder(root.right)

  def invert(self, root):
    if root is not None:
      self.invert(root.left)
      self.invert(root.right)

      temp = root.left
      root.left = root.right
      root.right = temp

tree = BST()
tree.root = tree.insert(tree.root, 5)
tree.insert(tree.root, 3)
tree.insert(tree.root, 7)
tree.insert(tree.root, 2)
tree.insert(tree.root, 1)
tree.insert(tree.root, 4)

tree.invert(tree.root)
tree.inOrder(tree.root)