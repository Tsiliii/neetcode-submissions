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
        else:
            lheight, rheight = self.height(root.left), self.height(root.right)
            self.d = max(self.d, lheight + rheight)
            return 1 + max(lheight, rheight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.height(root)
        return self.d