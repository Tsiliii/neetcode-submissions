class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity:int, weights: List[int], days:int) -> bool:
            current = 0
            solution = 1

            for x in weights:
                current += x
                if current > capacity:
                    solution += 1
                    current = x
            return solution <= days

        left = max(weights)
        right = sum(weights)

        while(left < right):
            mid = (left + right) // 2

            if possible(mid, weights, days):
                right = mid
            else:
                left = mid + 1

        return left