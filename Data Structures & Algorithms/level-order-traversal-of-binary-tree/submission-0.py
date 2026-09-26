# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append((root,0))
        answer = []
        level = 0
        current_answer = []
        while(queue):
            (node, current_level) = queue.popleft()
            if current_level > level:
                answer.append(current_answer)
                current_answer = []
                level = current_level
            current_answer.append(node.val)
            if node.left:
                queue.append((node.left, current_level+1))
            if node.right:
                queue.append((node.right, current_level+1))
        answer.append(current_answer)
        
        return answer