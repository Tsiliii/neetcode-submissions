class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = height[0], height[n-1]
        left = 1
        right = n-2

        answer = 0
        while(left <= right):
            if left_max < right_max:
                answer += max(min(left_max,right_max) - height[left], 0)
                left_max = max(left_max, height[left])
                left += 1
            else:
                answer += max(min(left_max,right_max) - height[right], 0)
                right_max = max(right_max, height[right])
                right -= 1
        return answer


        # left, right = [0] * len(height), [0] * len(height)
        # n = len(height)
        

        # for i in range(1,n):
        #     left[i] = max(left[i-1], height[i-1])
        # for i in range(n-2,-1, -1):
        #     right[i] = max(right[i+1], height[i+1])

        # answer = 0
        
        # for i in range(n):
        #     answer += max(min(left[i],right[i]) - height[i], 0)
        # return answer

    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     left = [0] * n
    #     right = [0] * n
    #     answer = 0

    #     for i in range(1,n):
    #         left[i] = max(left[i-1], height[i-1])

    #     for i in range(n-2, -1, -1):
    #         right[i] = max(right[i+1], height[i+1])

    #     for i in range(1, n-1):
    #         answer += max(min(left[i], right[i]) - height[i],0)
        
    #     return answer
