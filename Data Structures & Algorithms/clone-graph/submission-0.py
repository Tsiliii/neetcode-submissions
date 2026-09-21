"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone(self, node):
        if not node:
            return None
        elif node in self.clones:
            return self.clones[node]
        
        copy = Node(node.val)
        self.clones[node] = copy

        for neigh in node.neighbors:
            copy.neighbors.append(self.clone(neigh))
            
        return copy
        
        return
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.clones = {}
        return self.clone(node)
