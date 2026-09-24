class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals
        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals

        n = len(intervals)
        answer = []
        index = 0
        found = False
        
        def overlap(list1, list2):
            [x,y], [z,w] = list1, list2
            return  (x <= z and z<=y) or (x<= w and w <= y) or (z <= x and x <= w) or (z <= y and y <= w)
        # no overlap and new > 0
        # overlap
        # no overlap and new < 0
        while(index < n and not overlap(intervals[index],newInterval)) and intervals[index][1] < newInterval[0]:
            answer.append(intervals[index])
            index += 1

        while(index < n and overlap(intervals[index],newInterval)):
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        answer.append(newInterval)  

        while(index < len(intervals)):
            answer.append(intervals[index])
            index += 1
        
        return answer