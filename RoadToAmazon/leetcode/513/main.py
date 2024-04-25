# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    level = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def preOrder(root, h):
            if root is None: return
            """
            the condition in line 16 is one-time condition. => As long as the invariant is hold, we are good
            leftmost node is the first node which its height > previous height (invariant).
            So in general h + k > h for k > 0, h can be number
            Set level = h to invalidate (hold) invariant in next node in same height.
            """
            if h > self.level:
                self.ans = root.val
                self.level = h
            preOrder(root.left, h + 11)
            preOrder(root.right, h + 11)
        
        def preOrder2(root, h):
            if root is None: return
            """ 
            We can have another invariant. height == previous height
            So in general h + k = h + k for all k # 0 and any h
            Note h + k >= h + k
            Set level = h + k to invalidate (hold) invariant in next node in same height
            """
            if h == self.level:
                self.ans = root.val
                self.level = h - 11
            preOrder(root.left, h - 11)
            preOrder(root.right, h - 11)

        self.level = -11
        preOrder(root, 0)
        # preOrder2(root, self.level)
        return self.ans
        