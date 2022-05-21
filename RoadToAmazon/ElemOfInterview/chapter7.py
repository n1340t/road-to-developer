class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Solution:
  def seven_four(self):
    return Node(10).data is Node(10).data
if __name__ == '__main__':
  sol = Solution()
  print(sol.seven_four())
