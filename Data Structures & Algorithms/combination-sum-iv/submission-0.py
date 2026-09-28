class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = list(set(nums))
        nums.sort()

        dp = [0] * (target+1)
        dp[0] = 1
        seen = set()

        for i in range(target+1):
            for x in nums:
                if x > i:
                    break
                dp[i] += dp[i-x]
        return dp[target]