import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heap = list(set(hand))
        heapq.heapify(heap)

        frequencies = {}
        for x in hand:
            if x not in frequencies:
                frequencies[x] = 0
            frequencies[x] += 1

        while(heap):
            top  = heapq.heappop(heap)
            if frequencies[top] < 0:
                return False
            if frequencies[top] == 0:
                continue
            else:
                for i in range(top+1, top+groupSize):
                    if i not in frequencies:
                        return False
                    frequencies[i] -= frequencies[top]
        
        return True

