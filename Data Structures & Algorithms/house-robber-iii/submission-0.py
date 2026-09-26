# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root: Optional[TreeNode]) -> (int,int):
        if not root:
            return 0,0
        if not root.left and not root.right:
            return root.val, 0
        
        left_rob, left_not = self.rec(root.left)

        right_rob, right_not = self.rec(root.right)
        
        return (root.val + left_not + right_not, max(left_rob,left_not) + max(right_rob,right_not))

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rec(root))
        