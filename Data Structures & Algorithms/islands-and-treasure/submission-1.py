from collections import deque

class Solution:
    # def bfs(self, grid: List[List[int]], i: int, j: int, distance: int) -> None:
    #     if (i,j) in self.seen:
    #         return

    #     self.seen.add((i,j))

    #     if i > 0 and grid[i-1][j] > 0 and (i-1,j) not in self.seen:
    #         grid[i-1][j] = min(distance + 1, grid[i-1][j])
    #         self.dfs(grid, i-1, j, distance+1)

    #     if j > 0 and grid[i][j-1] > 0 and (i,j-1) not in self.seen:
    #         grid[i][j-1] = min(distance + 1, grid[i][j-1])
    #         self.dfs(grid, i, j-1, distance+1)

    #     if i < self.n -1 and grid[i+1][j] > 0 and (i+1,j) not in self.seen:
    #         grid[i+1][j] = min(distance + 1, grid[i+1][j])
    #         self.dfs(grid, i+1, j, distance+1)

    #     if j < self.m - 1 and grid[i][j+1] > 0 and (i,j+1) not in self.seen:
    #         grid[i][j+1] = min(distance + 1, grid[i][j+1])
    #         self.dfs(grid, i, j+1, distance+1)
    #     return

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.n, self.m = len(grid), len(grid[0])
        self.bfs_stack = deque([])
        self.seen = set()
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0:
                    self.bfs_stack.append((i,j,0))
        
        while(self.bfs_stack):
            i, j, distance = self.bfs_stack.popleft()
            if (i, j) in self.seen or i < 0 or i == self.n or j < 0 or j == self.m or grid[i][j] == - 1:
                continue
            self.seen.add((i,j))
            grid[i][j] = distance
            self.bfs_stack.append((i+1,j, distance + 1))
            self.bfs_stack.append((i,j+1, distance + 1))
            self.bfs_stack.append((i-1,j, distance + 1))
            self.bfs_stack.append((i,j-1, distance + 1))
        return