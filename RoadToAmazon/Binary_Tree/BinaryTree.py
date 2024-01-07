class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key
  def __repr__(self):
    return str(self.key)

if __name__ == '__main__':
  