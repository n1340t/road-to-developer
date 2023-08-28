'''
Using list to store nodes at each level
Similiar to dict, we make sure initialize at every index
'''
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return []
        def preOrder(root, level):
            # initialize list at every index
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)
            if root.left: preOrder(root.left, level + 1)
            if root.right: preOrder(root.right, level + 1)
            
        preOrder(root, 0)
        return res[::-1]