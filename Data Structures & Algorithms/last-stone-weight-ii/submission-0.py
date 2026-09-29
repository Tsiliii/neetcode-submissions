class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        answer = 0
        seen = {0}
        stones.sort()
        target = sum(stones) // 2

        for s in stones:
            iteratable = list(seen)
            for x in iteratable:
                if s+x <= target:
                    seen.add(s+x)
                    answer= max(answer, s+x)
        
        return sum(stones) - 2 * answer