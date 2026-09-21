from collections import deque
class Solution:
    def reachocean(self, heights, BFS_stack, ocean):
        n, m  = len(heights), len(heights[0])
        while(BFS_stack):
            i, j = BFS_stack.popleft()
            if (i, j) in ocean:
                continue 
            ocean.add((i,j))
            if i > 0 and heights[i-1][j] >= heights[i][j] and (i-1,j) not in ocean:
                BFS_stack.append((i-1,j))
            if j > 0 and heights[i][j-1] >= heights[i][j] and (i,j-1) not in ocean:
                BFS_stack.append((i,j-1))
            if i < n-1 and heights[i+1][j] >= heights[i][j] and (i+1,j) not in ocean:
                BFS_stack.append((i+1,j))
            if j < m-1  and heights[i][j+1] >= heights[i][j] and (i,j+1) not in ocean:
                BFS_stack.append((i,j+1))
        return ocean

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        atlanctic_BFS_stack = deque([])
        pacific_BFS_stack = deque([])
        n, m  = len(heights), len(heights[0])
        for i in range(n):
            pacific_BFS_stack.append((i,0))
            atlanctic_BFS_stack.append((i,m-1))
        for j in range(m):
            pacific_BFS_stack.append((0,j))
            atlanctic_BFS_stack.append((n-1,j))

        return list(self.reachocean(heights, atlanctic_BFS_stack, atlantic) & self.reachocean(heights, pacific_BFS_stack, pacific))

        # while(BFS_stack):
        #     i, j = BFS_stack.popleft()
        #     if (i, j) in pacific:
        #         continue 
        #     pacific.add((i,j))
        #     if i > 0 and heights[i-1][j] >= heights[i][j] and (i-1,j) not in pacific:
        #         BFS_stack.append((i-1,j))
        #     if j > 0 and heights[i][j-1] >= heights[i][j] and (i,j-1) not in pacific:
        #         BFS_stack.append((i,j-1))
        #     if i < n-1 and heights[i+1][j] >= heights[i][j] and (i+1,j) not in pacific:
        #         BFS_stack.append((i+1,j))
        #     if j < m-1  and heights[i][j+1] >= heights[i][j] and (i,j+1) not in pacific:
        #         BFS_stack.append((i,j+1))
        # return list(pacific)
                
