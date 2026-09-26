class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        if k > len(nums):
            k = len(nums) - 2

        seen = set()
        for i in range(k+1):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        for i in range(k+1,len(nums)):
            seen.remove(nums[i-(k+1)])
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False