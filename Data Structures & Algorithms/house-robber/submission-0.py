class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0] * (n+1)
        dp[n] = 0
        dp[n - 1] = nums[n - 1]

        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])
        
        return dp[0]