from collection import deque

graph = {
  '1': [],
  '2': []
}
n = 10 # number of nodes
distance = [0] * n
pi = [0] * n

root = '1'
q = deque(root)
while q:
  node = q.popleft()
  # for each child of graph node
  for x in graph[node]:
