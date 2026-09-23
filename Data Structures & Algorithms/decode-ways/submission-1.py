class Solution:
    
    def numDecodings(self, s: str) -> int:

        dp = [0 for _ in range(len(s) + 1)]
        dp[-1] = 1
        

        for i in range(len(s)-1, -1, -1):
            if i < len(s)-1 and ((s[i] == "2" and s[i+1] < "7" )or s[i] == "1"):
                dp[i] += dp[i+2]
            if s[i] != "0":
                dp[i] += dp[i+1]
        
        return dp[0]
