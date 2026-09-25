import random

class Solution:
    def partition(self, array):
        if len(array) <= 1:
            return array
        pivot = random.choice(array)
        left = []
        mid = []
        right = []

        for x in array:
            if x < pivot:
                left.append(x)
            elif x>pivot:
                right.append(x)
            else:
                mid.append(pivot)
        
        return self.partition(left) + mid + self.partition(right)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.partition(nums)
        