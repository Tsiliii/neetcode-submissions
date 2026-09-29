class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        current = []

        def backtrack(index, target, memo):
            if index == len(nums):
                return int(target == 0)

            key = (index,target)
            if key in memo:
                return memo[key]

            answer = 0
            # if target == 0:
                # answer += 1

            answer += backtrack(index+1, target + nums[index], memo)
            answer += backtrack(index+1, target - nums[index], memo)

            memo[key] = answer
            return answer
        
        return backtrack(0, target, {})