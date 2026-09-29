class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start = tank = total = 0
        # n = len(gas)

        # for i in range(n):
        #     diff = gas[i] - cost[i]
        #     total += diff
        #     tank += diff

        #     if tank < 0:
        #         start = i+1
        #         tank = 0

        # return start if total >= 0 else -1


        start = 0
        tank = gas[0]-cost[0]
        missing = 0

        for i in range(1,len(gas)):
            if tank < 0:
                missing -= tank
                start = i
                tank = 0
            tank += gas[i] - cost[i]

        return start if tank - missing >=0 else -1