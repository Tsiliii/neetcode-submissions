class Solution:
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