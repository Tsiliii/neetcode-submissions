class Solution:
    def bfs(self, grid, i, j):
        if (i,j) in self.seen:
            return 0
        self.seen.add((i,j))
        current = 0
        if i > 0 and grid[i-1][j] == 1 and (i-1, j) not in self.seen:
            current += 1 + self.bfs(grid, i-1, j)
        if j > 0 and grid[i][j-1] == 1 and (i, j-1) not in self.seen:
            current += 1 + self.bfs(grid, i, j-1)
        if i < self.n - 1 and grid[i+1][j] == 1 and (i+1, j) not in self.seen:
            current += 1 + self.bfs(grid, i+1, j)
        if j < self.m - 1 and grid[i][j+1] == 1 and (i, j+1) not in self.seen:
            current += 1 + self.bfs(grid, i, j+1)
        return current
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        self.seen = set()
        self.n = len(grid)
        self.m = len(grid[0])
        for i in range(self.n):
            for j in range(self.m):
                if (i,j) not in self.seen and grid[i][j] == 1:
                    answer = max(answer, 1 + self.bfs(grid, i, j))
                    
        return answer