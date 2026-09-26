class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n

        stack = [[temperatures[-1],n-1]]
        for i in range(n-2,-1,-1):
            today = temperatures[i]
            while stack and today >= stack[-1][0]:
                stack.pop()
            if stack:
                results[i] = stack[-1][1] - i
            stack.append([today,i])

        return results
