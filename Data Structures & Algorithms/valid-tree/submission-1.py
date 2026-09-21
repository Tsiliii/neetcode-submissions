class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        f = [i for i in range(n)]

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx != ry:
                f[rx] = ry
            return

        for x, y in edges:
            # print(f, x, y)
            if find(x) == find(y):
                return False
            union(x,y)
        return True
