class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = up = 0

        for char in s:
            if char == '(':
                lo += 1
                up += 1
            if char == ')':
                if up <= 0:
                    return False
                up -= 1
                lo -= 1
            if char == '*':
                up += 1
                lo = max(lo-1,0)

        return lo <= 0 <= up