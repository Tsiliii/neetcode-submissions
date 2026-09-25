class Solution:
    def reverseBits(self, n: int) -> int:
        # answer = 0
        # i = 31
        # while n:
        #     answer += (n & 1) * (2 ** i)
        #     i -= 1
        #     n >>= 1
        # return answer

        answer = 0
        i = 31
        while i >= 0:
            answer |= (n & 1) << i
            i -= 1
            n >>= 1
        return answer