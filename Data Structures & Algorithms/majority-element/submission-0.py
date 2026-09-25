class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for x in nums:
            if x == candidate:
                count += 1
            elif count == 0:
                candidate = x
                count += 1
            else:
                count -= 1
        return candidate