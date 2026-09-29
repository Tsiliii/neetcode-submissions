from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[0] != '0':
            return False
        
        BFS = deque([0])
        farthest = 0
        n = len(s)

        while BFS:
            i = BFS.popleft()
            if i == n-1:
                return True

            start = max(i + minJump, farthest+1)
            end = min(i+ maxJump, n-1)

            for j in range(start, end+1):
                if s[j] == '0':
                    BFS.append(j)
            
            farthest = max(farthest, end)
        return False