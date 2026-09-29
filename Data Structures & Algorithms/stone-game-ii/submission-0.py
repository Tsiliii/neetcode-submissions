class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        memo = {}

        def backtrack(i, M):
            if i == n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            best = float("-inf")
            total = 0

            for X in range(1, min(2 * M, n - i) + 1):
                total += piles[i + X - 1]

                best = max(
                    best,
                    total - backtrack(i + X, max(M, X))
                )

            memo[(i, M)] = best
            return best

        advantage = backtrack(0, 1)
        return (sum(piles) + advantage) // 2