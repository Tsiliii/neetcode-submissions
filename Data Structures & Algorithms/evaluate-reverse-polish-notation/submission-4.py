class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(0, len(tokens)):
            tok = tokens[i]
            if tok not in {"+", "-", "*", "/"}:
                stack.append(int(tok))
                continue

            num2 = stack.pop()
            num1 = stack.pop()

            if tok == '+':
                stack.append(num1 + num2)
            elif tok == '-':
                stack.append(num1 - num2)
            elif tok == '*':
                stack.append(num1 * num2)
            elif tok == '/':
                stack.append(int(num1 / num2))

        return stack[0]