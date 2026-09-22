class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return grid[0][0]
        edges = []
        n = len(grid)
        f = {}
        for i in range(n):
            for j in range(n):
                f[(i,j)] = (i,j)
                if i < n-1:
                    edges.append((max(grid[i+1][j], grid[i][j]), (i,j), (i+1,j)))
                if j < n-1:
                    edges.append((max(grid[i][j+1], grid[i][j]), (i,j), (i,j+1)))

        edges.sort()

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x,y):
            rx, ry = find(x), find(y)
            if rx != ry:
                f[ry] = rx
            return 

        index = 0
        while find((0,0)) != find((n-1,n-1)) :
            answer, x, y = edges[index]
            union(x,y)
            index += 1
        return answer