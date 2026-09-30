from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = deque()
        left = 0
        answer = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros.append(right)

            if len(zeros) > k:
                left = zeros.popleft() + 1

            answer = max(answer, right - left + 1)

        return answer