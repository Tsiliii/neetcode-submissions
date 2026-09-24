from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        queue = deque([])
        seen = set()
        queue.append(0)
        n = len(nums)

        while(queue):
            state = queue.popleft()
            if state >= n-1:
                return True 
            if state in seen:
                continue

            seen.add(state)
            for jump in range(1,nums[state]+1):
               queue.append(state+jump)

        return False