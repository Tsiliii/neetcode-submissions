class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        prev1, curr1 = 0, 0
        prev2, curr2 = 0, 0

        for i in range(n):
            # Scenario 1: Exclude the last house
            if i < n - 1:
                prev1, curr1 = curr1, max(curr1, prev1 + nums[i])

            # Scenario 2: Exclude the first house
            if i > 0:
                prev2, curr2 = curr2, max(curr2, prev2 + nums[i])

        return max(curr1, curr2)