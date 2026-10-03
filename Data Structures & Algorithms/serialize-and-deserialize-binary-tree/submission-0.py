# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        def dfs(root):
            if not root:
                output.append('N')
            else:
                output.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
                return

        dfs(root)
        return ",".join(output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        self.i = 0

        def dfs():
            val = data[self.i]
            self.i += 1

            if val == 'N':
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()