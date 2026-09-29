class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def answer(alice):
            if alice[0] > 0:
                return 'Alice'
            elif alice[0] == 0:
                return 'Tie'
            else:
                return 'Bob'

        n = len(stoneValue)
        alice = [0] * (n+1)
        bob = [0] * (n+1)
        # with 3 stones, Alices best option is either to take 1 in which case Bob will either take 1 or 2 and then subseq Alice can take 1 or none
        alice[n-1] = stoneValue[n-1]
        if n == 1:
            return answer(alice)
        alice[n-2] = max(stoneValue[n-2] - stoneValue[n-1], stoneValue[n-2] + stoneValue[n-1])
        if n == 2:
            return answer(alice)
        alice[n-3] = max(
            stoneValue[n-3] - alice[n-2],
            stoneValue[n-3] + stoneValue[n-2] - alice[n-1],
            stoneValue[n-3] + stoneValue[n-2] + stoneValue[n-1]
        )
        if n == 3:
            return answer(alice)
        for i in range(n-4, -1, -1):
            alice[i] = max(
                stoneValue[i] - alice[i+1],
                stoneValue[i] + stoneValue[i+1] - alice[i+2],
                stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - alice[i+3]
            )

        return answer(alice)