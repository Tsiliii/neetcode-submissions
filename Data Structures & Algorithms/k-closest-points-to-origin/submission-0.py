import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x,y in points:
            heapq.heappush(heap, [-1 * (x ** 2 + y ** 2), x, y])
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x,y] for _,x,y in heap]