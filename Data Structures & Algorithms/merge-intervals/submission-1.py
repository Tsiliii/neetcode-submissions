class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(ley = lambda x : x[0])

        answer = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= answer[-1][1]:
                answer[-1][1] = max(end, answer[-1][1])
            else:
                answer.append([start, end])

        return answer


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        answer = []
        for x,y in intervals[1:]:
            if end < x:
                answer.append([start, end])
                start, end = x,y
            else:
                end = max(end, y)
        answer.append([start,end])
        return answer