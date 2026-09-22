class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return costs[i]

        stairs = [sum(cost)] * (len(cost)+1)

        stairs[0] = cost[0]
        stairs[1] = cost[1]
        for i in range(2,len(cost)):
            stairs[i] = min(stairs[i-1], stairs[i-2]) + cost[i]

        return min(stairs[len(cost)-1], stairs[(len(cost) - 2)])