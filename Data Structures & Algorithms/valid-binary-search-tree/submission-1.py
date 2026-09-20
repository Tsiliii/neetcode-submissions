import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, root: Optional[TreeNode], LB, UB) -> bool:
        if not root:
            return True

        if root.val <= LB or root.val >= UB:
            return False
        return self.recursive(root.left, LB, min(UB, root.val)) and self.recursive(root.right, max(LB,root.val), UB)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower = -1 * math.inf
        upper = math.inf
        return self.recursive(root, lower, upper)