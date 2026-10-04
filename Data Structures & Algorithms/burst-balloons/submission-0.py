class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]

        # for i in range(n):
        #     dp[i][i] = nums[i]

        def recursive(left, right):
            if left + 1 == right:
                return 0
            if left == right or dp[left][right] != -1:
                return dp[left][right]
            
            answer = 0
            for i in range(left+1, right):
                answer= max(
                    answer, 
                    recursive(left, i)
                    + nums[left] * nums[i] * nums[right]
                    + recursive(i, right)
                    )
            dp[left][right] = answer
            return dp[left][right]

        recursive(0,n-1)
        return dp[0][n-1]