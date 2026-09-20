# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lheight, rheight = self.height(root.left), self.height(root.right)
        if abs(lheight - rheight) > 1:
            self.answer = False
        return 1 + max(lheight, rheight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        self.height(root)
        return self.answer