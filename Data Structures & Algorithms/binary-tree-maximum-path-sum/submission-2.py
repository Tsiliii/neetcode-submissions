# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        local_answer = max(-1001, root.val, root.val + left, root.val + right, root.val + left+ right)
        self.answer = max(local_answer, self.answer)
        return max(-1001, root.val, root.val + left, root.val + right)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = - 1001
        self.recursion(root)
        return self.answer