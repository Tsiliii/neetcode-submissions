class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current = answer = nums[0]

        for i in range(1, n):
            current = max(current + nums[i], nums[i])
            answer = max(answer, current)
        
        return answer