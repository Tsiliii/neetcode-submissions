class Solution:
    def recursion(self, text1:str, text2:str, i:int, j:int, dp:dict) -> int:
        key = (i,j)
        if i == len(text1) or j == len(text2):
            return 0
        elif key in dp:
            return dp[key]
        elif text1[i] == text2[j]:
            dp[key] = 1 + self.recursion(text1, text2, i+1, j+1, dp)            
        else:
            dp[key] = max(
                self.recursion(text1, text2, i+1, j, dp),
                self.recursion(text1, text2, i, j+1, dp)
            )
        return dp[key]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.recursion(text1, text2, 0, 0, {})

        n, m = len(text1), len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        return dp[0][0]

        # for i in range(n):
        #     dp[i][m] == 0
        # for j in rang(m):
        #     dp[n][j] == 0