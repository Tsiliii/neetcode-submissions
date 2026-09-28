class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        success = {n}

        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                word = s[i:j]
                if word in wordSet and j in success:
                    success.add(i)
                    break
        
        return 0 in success
                
