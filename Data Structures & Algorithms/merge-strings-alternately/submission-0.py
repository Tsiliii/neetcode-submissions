class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        answer = []
        for i in range(min(n,m)):
            answer.append(word1[i])
            answer.append(word2[i])
        answer = "".join(answer)
        if n < m:
            return answer + word2[n:]
        elif n > m:
            return answer + word1[m:]
        else:
            return answer
