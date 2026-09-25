import random

class Solution:
    def quicksort(self, nums: List[int], lo: int, hi: int) -> None:
        if lo >= hi:
            return

        pivot = nums[random.randint(lo, hi)]
        left = mid = lo
        right = hi

        while(mid <= right):

            if nums[mid] > pivot:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1

            elif nums[mid] < pivot:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            else:
                mid += 1 
        
        self.quicksort(nums, lo, left-1)
        self.quicksort(nums, right+1, hi)

        return

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)
        return 