# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def comp_size(self, root):
        if not root:
            return 0
        return 1 + self.comp_size(root.left) + self.comp_size(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left_size = self.comp_size(root.left)
        right_size = self.comp_size(root.right)

        if left_size == k-1:
            return root.val
        elif left_size < k-1:
            return self.kthSmallest(root.right, k-left_size -1)
        else:
            return self.kthSmallest(root.left, k)