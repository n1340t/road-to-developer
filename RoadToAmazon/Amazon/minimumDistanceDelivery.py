from collections import deque
'''
Think of calculating the "tree height" for the graph.
- we used BFS (level-order) to calculate the height of binary tree. Since binary tree is a special kind
of graph, we can apply the same idea.
For this problem, BFS is prefer because BFS is really good for shortest path
When it reaches to destination, it will reach to certain height, we need to find that height which the length of the path
'''
class Solution:
    def __init__(self):
        self.city_map = [[1, 1, 0], [1, 0, 0], [1, 9, 1]]
    def set_city_map(self, city_map):
      self.city_map = city_map

    def minimumDistance(self):
        dist = 0 #level of maze (tree)
        q = deque([(0,0)])
        self.city_map[0][0] = 0
        moveC = (-1, 1, 0, 0)
        moveR = (0, 0, -1, 1)
        row_len = len(self.city_map[0])
        col_len = len(self.city_map)
        while q:
          dist += 1
          n = len(q)
          for _ in range(n):
            row, col = q.popleft()
            for i in range(4):
              next_col = col + moveC[i]
              next_row = row + moveR[i]
              if 0 <= next_col < col_len and 0 <= next_row < row_len and self.city_map[next_row][next_col] != 0:
                if self.city_map[next_row][next_col] == 9:
                  return dist
                q.append((next_row, next_col))
                self.city_map[next_row][next_col] = 0
        return dist


sol = Solution()
print(sol.minimumDistance())