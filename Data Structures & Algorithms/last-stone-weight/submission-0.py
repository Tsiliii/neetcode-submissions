import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for x in stones:
            heapq.heappush(heap, -1 * x)

        while(len(heap)) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -1 * abs(y-x))

        return 0 if len(heap) == 0 else -1 * heap[0]