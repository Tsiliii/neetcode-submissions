import math

class Solution:
    def eat_within_h(self, piles: List[int], h: int, serving: int) -> bool:
        time = 0
        for i in range(len(piles)):
            time += (math.ceil(piles[i] / serving))
            if time > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = max(1, math.ceil(sum(piles) / h))
        right = max(piles) + 1

        while(left < right):
            mid = (left + right) // 2

            if self.eat_within_h(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return left