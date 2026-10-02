class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [0] * (amount + 1)
        # dp[0] = 1
        # for c in coins:
        #     for i in range(amount+1):
        #         if i - c >= 0:
        #             dp[i] += dp[i-c]
  
        # return dp[amount]

        memo = {}

        def backtrack(i, remaining):
            if remaining == 0:
                return 1

            if remaining < 0 or i == len(coins):
                return 0

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            take = backtrack(i, remaining - coins[i])
            skip = backtrack(i + 1, remaining)

            memo[(i, remaining)] = take + skip
            return memo[(i, remaining)]

        return backtrack(0, amount)
