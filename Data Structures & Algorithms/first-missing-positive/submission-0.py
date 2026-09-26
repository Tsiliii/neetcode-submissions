class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0
        n = len(nums)
        while i < n:
            x = nums[i]
            if x != i+1 and 1 <= x <= n and nums[x-1] != x:
                nums[x-1], nums[i] = x, nums[x-1]
            else:
                i += 1

        for i in range(0,len(nums)):
            if nums[i]-1 != i:
                return i + 1
        return len(nums) + 1