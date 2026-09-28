class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1,int(n ** 0.5)+1):
            nums.append(i ** 2)

        dp = [n+1] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(1,n+1):
            for x in nums:
                if x > i:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i-x] + 1)

        return dp[n]