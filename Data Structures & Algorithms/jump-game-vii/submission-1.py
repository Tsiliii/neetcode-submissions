from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[0] != '0':
            return False
        
        BFS = deque([0])
        seen = set()
        n = len(s)
        while BFS:
            i = BFS.popleft()
            if i == n-1:
                return True
            if i in seen:
                continue
            seen.add(i)            
            for j in range(min(i+ maxJump, n - 1), i + minJump-1, -1):
                if s[j] == '0' and j not in seen:
                    BFS.append(j)
        return False