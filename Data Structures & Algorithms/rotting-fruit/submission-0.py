class Solution:
    def BFS_expand(self, grid, BFS, m, n, i, j, distance):
        if i > 0 and grid[i-1][j] == 1:
            BFS.append([i-1,j,distance + 1])
            grid[i-1][j] = 2
        if i < m-1 and grid[i+1][j] == 1:
            BFS.append([i+1,j,distance + 1])
            grid[i+1][j] = 2
        if j > 0 and grid[i][j-1] == 1:
            BFS.append([i,j-1,distance + 1])
            grid[i][j-1] = 2
        if j < n-1  and grid[i][j+1] == 1:
            BFS.append([i,j+1,distance + 1])
            grid[i][j+1] = 2
        return
        # if i > 0 and j > 0 and grid[i-1][j-1] == 1:
        #     BFS.append([i-1,j-1,distance + 1])
        #     grid[i-1][j-1] = 2
        # if i > 0 and j < n-1  and grid[i-1][j+1] == 1:
        #     BFS.append([i-1,j+1,distance + 1])
        #     grid[i-1][j+1] = 2
        # if i < m-1 and j > 0 and grid[i+1][j-1] == 1:
        #     BFS.append([i+1,j-1,distance + 1])
        #     grid[i+1][j-1] = 2
        # if i < m-1 and j < n-1 and grid[i+1][j+1] == 1:
        #     BFS.append([i+1,j+1,distance + 1])
        #     grid[i+1][j+1] = 2
        # return

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        BFS = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    BFS.append([i,j,0])

        answer = 0
        while BFS:
            i,j,distance = BFS.popleft()
            # print(i,j,distance)
            answer = max(answer, distance)
            self.BFS_expand(grid, BFS, m, n, i, j, distance)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return answer
