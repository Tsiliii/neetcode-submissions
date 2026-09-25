class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) -1
        carry = 1
        while(carry != 0):
            if i < 0:
                return [1] + digits
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
            i -= 1
        return digits