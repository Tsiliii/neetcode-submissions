class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        answer = n
        for i in range(n):
            answer = answer ^ i ^ nums[i]

        return answer

        # n = len(nums)
        # answer = n * (n+1) //2
        # return answer - sum(nums)