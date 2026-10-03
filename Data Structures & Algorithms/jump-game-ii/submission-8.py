import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jumps = 0
        next_farthest = 0

        for i in range(len(nums)-1):
            next_farthest = max(next_farthest, i + nums[i])

            if i == farthest:
                farthest = next_farthest
                jumps += 1
        return jumps


    # def jump(self, nums: List[int]) -> int:
    #     # n = len(nums)
    #     # dp = [math.inf] * (n+1)
    #     # dp[n-1] = 0

    #     # for i in range(n-1, -1, -1):
    #     #     for j in range(1,nums[i]+1):
    #     #         if i+j < n:
    #     #             dp[i] = min(dp[i+j] + 1, dp[i])
    #     # return dp[0]

    #     n = len(nums)
    #     # if n == 1:
    #     #     return 0
    #     next_far = 0
    #     answer = 0

    #     i = 0
    #     while(next_far < n-1):
    #         answer += 1
    #         farthest = next_far
    #         while (i <= farthest):
    #             next_far = max(i + nums[i], next_far)
    #             i += 1

    #     return answer

