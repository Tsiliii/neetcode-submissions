"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heap = []
        answer = 0

        for interval in intervals:
            x,y = interval.start, interval.end
            while heap and heap[0] <= x:
                heapq.heappop(heap)

            heapq.heappush(heap, y)
            answer = max(answer, len(heap))

        return answer

    # def minMeetingRooms(self, intervals: List[Interval]) -> int:
    #     if not intervals:
    #         return 0
    #     intervals.sort(key = lambda x: x.start)

    #     heap = []
    #     answer = 0

    #     for interval in intervals:
    #         while heap and heap[0] <= interval.start:
    #             heapq.heappop(heap)

    #         heapq.heappush(heap, interval.end)
    #         answer = max(answer, len(heap))

    #     return answer