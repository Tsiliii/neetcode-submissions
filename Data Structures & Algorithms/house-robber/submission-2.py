class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        second = 0
        first = nums[n - 1]

        for i in range(n-2, -1, -1):
            current = max(first, second + nums[i])
            second = first
            first = current
        
        return first