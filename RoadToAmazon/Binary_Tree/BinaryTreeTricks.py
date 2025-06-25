from collections import deque

class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key
  def __repr__(self):
    return str(self.key)

class BinaryTree:
  def __init__(self):
    self.root = None
  
  '''
  Trick 1: Traverse the tree and store result in a list.
  We can't declare a property in BinaryTree class. We want to test the method multiple times. Class property won't be reset in next excution.
  '''
  def inOrderTraversal(self, root: Optional[Node]) -> List[int]:
    def helper(root, result):
      if root is None:
        return result
      helper(root.left, result)
      result.append(root.value)
      helper(root.right, result)
      return result
    return helper(root, [])
  # inOrder traversal - iterative (simulate call stack)
  def inOrderTraversal(self, root: Optional[Node]) -> List[int]:
    res = []
    stack = deque(root)
    while stack:
      if stack[-1]:
        stack.append(node.left)
      
if __name__ == '__main__':
  