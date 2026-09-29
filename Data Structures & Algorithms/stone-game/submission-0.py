class Solution:
    def recursive(self, piles, left, right, memo):
        key = (left,right)
        if key in memo:
            return memo[key]
        else:
            answer = max(
                piles[left] - self.recursive(piles, left+1, right, memo),
                piles[right] - self.recursive(piles, left, right-1, memo)
                )
            memo[key] = answer
            return memo[key]

    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        for i, p in enumerate(piles):
            dp[(i,i)] = p

        return self.recursive(piles, 0,0, dp) > 0