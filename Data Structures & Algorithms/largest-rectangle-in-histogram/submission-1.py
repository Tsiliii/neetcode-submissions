class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = max(heights)
        stack = [[heights[0],0]]

        for i in range(1,len(heights)):
            index = i
            while stack and stack[-1][0] >= heights[i]:
                h, pos = stack.pop()
                answer = max(answer, h * (i - pos))
                index = pos
            
            stack.append([heights[i], index])
            
            i += 1

        for h, pos in stack:
            answer = max(answer, h * (len(heights)-pos))


        return answer
            