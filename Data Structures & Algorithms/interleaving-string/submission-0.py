class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s2 == "":
            return s1 == s3
        if s1 == "":
            return s2 == s3

        n = len(s1)
        m = len(s2)
        if len(s3) != n + m:
            return False

        dp = [[False] * (m+1) for _ in range(n+1)]
        
        dp[n][m] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                # character = s3[i+j]

                if i < n and s1[i] == s3[i + j]:
                    dp[i][j] |= dp[i + 1][j]

                if j < m and s2[j] == s3[i + j]:
                    dp[i][j] |= dp[i][j + 1]

        return dp[0][0]