class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        leaves = set()
        nodes = set()
        adj = {}

        for u,v in edges:
            if u not in adj:
                adj[u] = {v}
                nodes.add(u)
                leaves.add(u)
            else:
                adj[u].add(v)
                if u in leaves:
                    leaves.remove(u)
            if v not in adj:
                adj[v] = {u}
                nodes.add(v)
                leaves.add(v)
            else:
                adj[v].add(u)
                if v in leaves:
                    leaves.remove(v)

        while len(nodes) > 2:
            new_leaves = set()
            for leaf in leaves:
                for neighbor in adj[leaf]:
                    adj[neighbor].remove(leaf)
                    if len(adj[neighbor]) == 1:
                        new_leaves.add(neighbor)
                nodes.remove(leaf)
            leaves = new_leaves

        return list(leaves)
