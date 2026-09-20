import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myheap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.myheap, val)

        if len(self.myheap) > self.k:
            heapq.heappop(self.myheap)

        return self.myheap[0]
        
