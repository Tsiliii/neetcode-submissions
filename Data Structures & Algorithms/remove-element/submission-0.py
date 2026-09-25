class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while(left <= right):
            if nums[left] != val:
                left += 1
            elif nums[right] == val:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
        return left
                