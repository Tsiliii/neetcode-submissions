class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find array split
        left = 0
        right = len(nums) - 1
        
        while(left < right):
            mid = (left + right) // 2
            
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        min_index = left
        if target <= nums[-1]:
            left, right = min_index, len(nums)
        else:
            left, right = 0, min_index
        # print(min_index)
        while(left < right):
            mid = (left + right) // 2
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid 
        if left < len(nums) and nums[left] == target:
            return left
        return -1
