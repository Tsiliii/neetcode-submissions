class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        minimum_buy = prices[0]
        for i in range(1,len(prices)):
            answer = max(answer, prices[i] - minimum_buy)
            minimum_buy = min(minimum_buy, prices[i])
        return answer
        # n = len(prices)
        # left = [0] * n
        # left[0] = prices[0]

        # for i in range(1,n):
        #     left[i] = min(left[i-1], prices[i])
        
        # answer = 0
        # for i in range(n-1,0,-1):
        #     answer = max(answer, prices[i] - left[i-1])
        
        # return answer