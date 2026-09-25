class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        a &= mask
        b &= mask
        answer = 0
        carry = 0
        for i in range(32):
            a_bit = a & 1
            b_bit = b & 1

            if a_bit or b_bit or carry:
                answer |= (1 << i) * (a_bit^b_bit^carry)
            if (a_bit and b_bit) or (a_bit and carry) or (b_bit and carry):
                carry = 1
            else:
                carry = 0

            a >>= 1
            b >>= 1

        if answer >= (1 << 31):
            return answer - (1 << 32)
        return answer
