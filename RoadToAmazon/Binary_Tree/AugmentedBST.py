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

  def unrank(self, node, k):
    print(node, k)
    if k == node.lCount:
      return node
    elif k < node.lCount:
      return self.unrank(node.left, k)
    else:
      return self.unrank(node.right, k - node.lCount - 1) #subtract right node itself
  # select = unrank
  def select(self, root, k):
    # Base case
    if (root == None):
        return None
         
    count = root.lCount + 1
     
    if (count == k):
        return root
 
    if (count > k):
        return self.kthSmallest(root.left, k)
 
    # Else search in right subtree
    return self.kthSmallest(root.right, k - count)

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
  tree.inOrder(tree.root)
  # print(tree.select(tree.root, 1))
  # print(tree.unrank(tree.root, 1))