class Solution:
    def check(self, s, i, j):
        while(i < j):
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                break    
        return i,j

    def validPalindrome(self, s: str) -> bool:
        i, j = self.check(s, 0, len(s)-1)
        if i >= j:
            return True
        else:
            left, right = self.check(s, i+1, j)
            if left >= right:
                return True
            left, right = self.check(s, i, j-1)
            if left >= right:
                return True
            return False
