class Solution:
    def checkValidString(self, s: str) -> bool:
        # difference = 0
        # stars = 0
        # for char in s:
        #     if char == "(":
        #         difference += 1
        #     elif char == ")":
        #         difference -= 1
        #     else:
        #         stars += 1

        #     if difference < 0:
        #         if stars == 0:
        #             return False
        #         difference = 0
        #         stars -= 1

        # return difference <= stars

        lo = up = 0

        for char in s:
            if char == '(':
                lo += 1
                up += 1
            elif char == ')':
                if up <= 0:
                    return False
                up -= 1
                lo = max(lo-1,0)
            elif char == '*':
                up += 1
                lo = max(lo-1,0)

        return lo == 0 