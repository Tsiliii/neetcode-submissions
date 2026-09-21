class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []
        current = []

        index = 0

        def search(nums, target, index):
            if target == 0:
                answer.append(current.copy())
                return
            if target > 0:
                current.append(nums[index])
                search(nums, target-nums[index], index)
                current.pop()
            for i in range(index+1,len(nums)):
                if target - nums[i] < 0:
                    break
                current.append(nums[i])
                search(nums, target - nums[i], i)
                current.pop()
            return

        search(nums, target, 0)
        return answer
