'''
There are two main factors here:
1. From left to right
2. and top to bottom

to achieve 1 we can use in order traversal
to achieve 2 we can use level  order traversal.

It's easier to do 2 first and 1 later because sorting the key is much easier job. (OrderedMap, etc.)
https://www.geeksforgeeks.org/vertical-order-traversal-of-binary-tree-using-map/
https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/
'''
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        if not root: return []
        root.level = 0
        q = deque([root])
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                res[node.level].append(node.val)
                if node.left:
                    node.left.level = node.level - 1
                    q.append(node.left)
                if node.right:
                    node.right.level = node.level + 1
                    q.append(node.right)

        return [v for k, v in sorted(res.items())]