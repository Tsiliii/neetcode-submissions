from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        answer = []

        i = 0
        n = len(nums)

        while i < n:
            
            current = nums[i]

            while queue and queue[0][1] <= i - k:
                queue.popleft()

            while queue and queue[-1][0] <= current:
                queue.pop()

            # if not queue or queue[-1][0] < current:
            queue.append((current, i))

            if i >= k-1:
                answer.append(queue[0][0])
            
            i += 1

        return answer


        # heap = []
        # heapq.heapify(heap)

        # freq = {}

        # for i in range(k):
        #     freq[nums[i]] = freq.get(nums[i],0) + 1
        #     heapq.heappush(heap, -1 * nums[i])
        
        # answer = [min(nums)] * (len(nums) - k + 1)
        # for i in range(k, len(nums)+1):
        #     while(heap and freq[-1 * heap[0]] == 0 ):
        #         heapq.heappop(heap)
        #     answer[i - k] = -1 * heap[0]
        #     freq[nums[i-k]] -= 1

        #     if i == len(nums):
        #         break
        #     freq[nums[i]] = freq.get(nums[i],0) + 1
        #     heapq.heappush(heap, -1 * nums[i])

        # return answer