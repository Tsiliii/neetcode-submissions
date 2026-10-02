import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        heap = [-1 * value for _, value in freq.items()]
        heapq.heapify(heap)
        queue = deque([])
        time = 0

        while heap or queue:

            if not heap and queue[0][0] > time:
                time = queue[0][0]
                continue

            while queue and time >= queue[0][0]:
                _, neg_freq = queue.popleft()
                heapq.heappush(heap, neg_freq)
            
            neg_freq = heapq.heappop(heap)
            neg_freq += 1
            if neg_freq < 0:
                queue.append([time + n+1, neg_freq])
            time += 1

        return time
            
