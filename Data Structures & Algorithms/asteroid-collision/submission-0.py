class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:
            alive = True
            if x < 0:
                if not stack or stack[-1] < 0:
                    stack.append(x)
                else:
                    while stack and stack[-1] > 0:
                        if abs(x) > stack[-1]:
                            stack.pop()
                        elif abs(x) == stack[-1]:
                            alive = False
                            stack.pop()
                            break
                        else:
                            alive = False
                            break
                    if alive:
                        stack.append(x)
            else:
                stack.append(x)
            
        return stack
            