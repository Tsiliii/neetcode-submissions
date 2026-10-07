import math

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [math.inf] * (len(days)+1)

        dp[-1] = 0

        for i in range(len(days) -  1, -1, -1):
            dp[i] = costs[0] + dp[i+1]
            
            # 7-day: find first uncovered day
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            week = costs[1] + dp[j]

            # 30-day: find first uncovered day
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            month = costs[2] + dp[j]

            dp[i] = min(dp[i], week, month)

        return dp[0]