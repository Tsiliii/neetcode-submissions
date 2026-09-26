class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        def index(char):
            return ord(char) - ord('a')

        s1_rep = [0] * 26

        for char in s1:
            s1_rep[index(char)] += 1
        
        s2_rep = [0] * 26

        for i in range(len(s1)):
            s2_rep[index(s2[i])] += 1

        j = len(s1)
        while(j < len(s2)):
            if s1_rep == s2_rep:
                return True
            s2_rep[index(s2[j - len(s1)])] -= 1
            s2_rep[index(s2[j])] += 1
            j += 1 
        return s1_rep == s2_rep
            