class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def max_array(nums):
            answer = current = nums[0]

            for i in range(1,len(nums)):
                x = nums[i]
                current = max(current + x, x)
                answer = max(answer,current)
            return answer

        no_loop = max_array(nums)
        loop = sum(nums) + max_array([-x for x in nums])
        return max(no_loop, loop) if no_loop >= 0 else no_loop