class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while (n > 0):
            answer += (n % 2)
            n = n // 2
        return answer 