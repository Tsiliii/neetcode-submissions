from collections import deque
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        queue = deque([])
        queue.append((amount,0))

        while(queue):
            state, used = queue.popleft()
            if state < 0:
                continue
            
            if dp[state] > used:
                dp[state] = used
                for c in coins:
                    queue.append((state-c, used+1))

        return dp[0] if dp[0] != math.inf else -1
