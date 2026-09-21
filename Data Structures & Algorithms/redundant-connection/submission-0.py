class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for x,y in edges:
            n = max(n,x,y)
        f = [i for i in range(n+1)]

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
            if find(x) == find(y):
                return [x,y]
            union(x,y)
        return
                    