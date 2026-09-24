import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * (n+1)
        dp[n-1] = 0

        for i in range(n-1, -1, -1):
            for j in range(1,nums[i]+1):
                if i+j < n:
                    dp[i] = min(dp[i+j] + 1, dp[i])
        return dp[0]