from collections import deque

class Solution:
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