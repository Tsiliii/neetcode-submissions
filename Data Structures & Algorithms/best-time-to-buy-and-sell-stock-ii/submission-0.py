class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        one, zero = 0, 0
        
        for i in range(n-1,-1,-1):
            zero, one = max(one - prices[i], zero), max(one, zero + prices[i])

        return zero
