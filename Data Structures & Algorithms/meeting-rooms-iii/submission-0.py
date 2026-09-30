import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        occupied = []  # (end_time, room_number)
        count = [0] * n

        for start, end in meetings:

            # Release all rooms available by the meeting's start time.
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            duration = end - start

            if available:
                # Assign the smallest-numbered available room.
                room = heapq.heappop(available)
                new_end = end

            else:
                # Delay the meeting until the earliest room becomes free.
                earliest_end, room = heapq.heappop(occupied)
                new_end = earliest_end + duration

            heapq.heappush(occupied, (new_end, room))
            count[room] += 1

        return count.index(max(count))