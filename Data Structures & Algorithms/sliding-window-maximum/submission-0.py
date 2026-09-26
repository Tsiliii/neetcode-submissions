import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        freq = {}

        for i in range(k):
            freq[nums[i]] = freq.get(nums[i],0) + 1
            heapq.heappush(heap, -1 * nums[i])
        
        answer = [min(nums)] * (len(nums) - k + 1)
        for i in range(k, len(nums)+1):
            while(heap and freq[-1 * heap[0]] == 0 ):
                heapq.heappop(heap)
            answer[i - k] = -1 * heap[0]
            freq[nums[i-k]] -= 1

            if i == len(nums):
                break
            freq[nums[i]] = freq.get(nums[i],0) + 1
            heapq.heappush(heap, -1 * nums[i])

        return answer