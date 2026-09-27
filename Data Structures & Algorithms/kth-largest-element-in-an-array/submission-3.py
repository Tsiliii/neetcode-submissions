import random
import heapq

class Solution:
    def partition(self, nums: List[int], k: int) -> int:
        if len(nums) == k:
            return min(nums)

        pivot = random.choice(nums)
        left = []
        right =  []
        mid = 0

        for x in nums:
            if x < pivot:
                left.append(x)
            elif x>pivot:
                right.append(x)
            else:
                mid += 1
            
        if len(right) >= k:
            return self.partition(right, k)
        elif len(right) + mid >= k:
            return pivot
        else:
            return self.partition(left, k - len(right) - mid)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return self.partition(nums, k)

        heap = []
        heapq.heapify(heap)

        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return min(heap)