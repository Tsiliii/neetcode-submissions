class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n+1)
        if n == 0:
            return dp
        dp[1] = 1
        power = 2
        i = 2
        while(i <= n):
            for j in range(power):
                if i + j > n:
                    break
                dp[i+j] = dp[j] + 1
            i = i + power
            power *= 2
        return dp
            
