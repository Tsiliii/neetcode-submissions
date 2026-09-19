class Solution:
    # def recursive(self, s: str, left: int, right: int) -> bool:
    #     if right > len(s):
    #         return False
    #     if left == right:
    #         return True
    #     next_two = s[left:left+2]
    #     if next_two == '()' or next_two == '[]' or next_two == "{}":
    #         return self.recursive(s, left+2, right)
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
                continue
            if not stack:
                return False
            top = stack.pop()
            if (s[i] == ')' and top != '(') or (s[i] == '}' and top != '{') or (s[i] == ']' and top != '['):
                return False
        return (len(stack) == 0)
