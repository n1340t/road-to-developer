class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
  
  def __repr__(self):
    return str(self.key)

# Stanford implemtation

class BST:
  def __init__(self):
    self.root = None
  # return the last node before went off the tree
  def search(self, key):
    x = self.root
    while(x is not None):
      if (key < x.key):
        if x.left is None: return x
        else: x = x.left
      elif (key > x.key):
        if x.right is None: return x
        else: x = x.right
      else: return x

  def searchV2(self, node, key):
    if node.key == key:
      return node
    elif key < node.key:
      if node.left is None: return node
      return self.searchV2(node.left, key)
    elif key > node.key:
      if node.right is None: return node
      return self.searchV2(node.right, key)

  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
      return self.root

    x = self.searchV2(self.root, key)
    if key < x.key:
      x.left = Node(key)
    elif key > x.key:
      x.right = Node(key)

  def inOrderTraversal(self, node):
    if node is not None:
      self.inOrderTraversal(node.left)
      print('key', node)
      self.inOrderTraversal(node.right)

  def isBST(self, root, min_node, max_node):
    if root is None: return True
    if min_node is not None and root.key <= min_node.key: return False
    if max_node is not None and root.key >= max_node.key: return False
    # root is max_node of root.left because all left node (root.left) (in subtree as well) must <= root
    # root is min_node of root.right because all right node (root.left) must >= root
    return self.isBST(root.left, min_node, root) and self.isBST(root.right, root, max_node)

  # the idea in v2 is slightly different
  def isBSTv2(self, node, parent_left, parent_right):
    print(node, parent_left, parent_right)
    if node is None: return True
    if parent_left and parent_left.key <= node.key: return False
    if parent_right and parent_right.key >= node.key: return False
    return self.isBSTv2(node.left, node, parent_right) and self.isBSTv2(node.right, parent_left, node)

  def height(self, root):
    if root is None: return 0
    return 1 + max(self.height(root.left), self.height(root.right))

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(1)
tree.insert(4)
# tree.inOrderTraversal(tree.root)
res = tree.isBSTv2(tree.root, None, None)
print(res)