class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        dp = [[1] * m for _ in range(n)]

        cells = [
            (matrix[i][j], i, j)
            for i in range(n)
            for j in range(m)
        ]

        cells.sort()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for value, i, j in cells:
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < n
                    and 0 <= nj < m
                    and matrix[ni][nj] > value
                ):
                    dp[ni][nj] = max(
                        dp[ni][nj],
                        dp[i][j] + 1
                    )

        return max(max(row) for row in dp)