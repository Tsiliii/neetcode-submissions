class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
            union(x,y)

        answer = set()
        for x in range(n):
            answer.add(find(x))
        return len(answer)
