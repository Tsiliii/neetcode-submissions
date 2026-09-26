# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, root: Optional[TreeNode], val:int) -> Optional[TreeNode]:
        if root.val < val:
            if root.right:
                self.recursion(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left:
                self.recursion(root.left, val)
            else:
                root.left = TreeNode(val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        answer = root
        while True:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return answer
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return answer
