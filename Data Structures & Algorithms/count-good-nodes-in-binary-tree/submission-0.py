# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursion(self, root: TreeNode, maxseen: int) -> int:
        if not root:
            return 0
        return int(root.val >= maxseen) + self.recursion(root.left, max(maxseen,root.val)) + self.recursion(root.right, max(maxseen,root.val))

    def goodNodes(self, root: TreeNode) -> int:
        return self.recursion(root, -101)
        