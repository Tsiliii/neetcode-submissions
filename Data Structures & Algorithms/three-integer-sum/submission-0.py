class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = set()
        for i in range(n-1):
            target = -1 * nums[i]
            seen = set()
            seen.add(target - nums[i + 1])
            for j in range(i+2, n):
                if nums[j] in seen:
                    sorted_tuple = tuple(sorted([nums[i], target - nums[j], nums[j]]))
                    answer.add(sorted_tuple)
                if target - nums[j] not in seen:
                    seen.add(target - nums[j])
        return [list(ans) for ans in answer]
                
