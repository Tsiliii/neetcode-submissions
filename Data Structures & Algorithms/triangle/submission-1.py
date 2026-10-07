import math
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[math.inf] * (n+1) for _ in range(n)]

        for i in range(n):
            dp[-1] = triangle[-1]

        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j] = triangle[i][j] + min(
                    dp[i+1][j],
                    dp[i+1][j+1] if j <= i else math.inf,
                    # dp[i+1][j-1] if j - 1 >= 0 else math.inf,
                    )

        return dp[0][0]