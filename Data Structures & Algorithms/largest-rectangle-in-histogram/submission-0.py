class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = max(heights)
        stack = [[heights[0],0]]
        i = 1

        while(i < len(heights)):
            index = i
            while stack and stack[-1][0] >= heights[i]:
                _, index = stack.pop()
            
            answer = max(answer, heights[i] * (i-index + 1))
            for h, pos in stack:
                answer = max(answer, h * (i-pos + 1))
            stack.append([heights[i], index])
            
            i += 1
        return answer
            