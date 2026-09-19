class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        answer = 0

        for i in range(1,n):
            left[i] = max(left[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])

        for i in range(1, n-1):
            answer += max(min(left[i], right[i]) - height[i],0)
        
        return answer
