class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        characters = {}
        for i in range(n):
            if s[i] not in characters:
                characters[s[i]] = 0
            if t[i] not in characters:
                characters[t[i]] = 0
            
            characters[s[i]] += 1
            characters[t[i]] -= 1

        for _, value in characters.items():
            if value != 0:
                return False
        
        return True
            
            
