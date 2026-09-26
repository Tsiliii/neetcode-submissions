# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.answer.append(root.val)
        self.recursive(root.left)
        self.recursive(root.right)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.recursive(root)
        return self.answer