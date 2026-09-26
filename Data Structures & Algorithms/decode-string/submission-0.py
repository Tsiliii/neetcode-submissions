class Solution:
    def decodeString(self, s: str) -> str:
        current = ""
        stack = []
        i = 0
        while (i < len(s)):
            if s[i].isdigit():
                if s[i+1].isdigit() and s[i+2].isdigit():
                    iterations = int(s[i:i+3])
                    i += 4
                elif s[i+1].isdigit():
                    iterations = int(s[i:i+2])
                    i += 3
                else:
                    iterations = int(s[i])
                    i += 2
                stack.append([current, iterations])
                current = ""
            elif s[i].islower():
                current += s[i]
                i += 1
            elif s[i] == "]":
                previous, iterations = stack.pop()
                current = previous + current * iterations
                i += 1
        return current 

