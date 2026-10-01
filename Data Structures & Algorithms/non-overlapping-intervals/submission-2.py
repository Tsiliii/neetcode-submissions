class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        answer = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            if next_start >= end:
                end = next_end
            else:
                answer += 1
                end = min(end, next_end)
        return answer

    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        answer = 0
        start, end = intervals[0]

        i = 1
        while(i < len(intervals)):

            left, right = intervals[i]
            if end <= left:
                start, end = left, right 
            else:
                answer += 1
                if end > right:
                    start, end = left, right
            i += 1
        return answer