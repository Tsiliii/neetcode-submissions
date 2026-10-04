class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[x] = best produce i can get when breaking x
        # = max_1<i<n i * dp[x-i], i * (x-i)

        dp = [0] * (n+1)
        dp[1] = 1
        for x in range(1, n+1):
            for i in range(1, x):
                dp[x] = max(dp[x], i * dp[x-i], i * (x-i))

        return dp[n]