class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        answer = []
        current = []

        def backtrack(i):
            if i == len(s):
                answer.append(" ".join(current))
                return

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]

                if word in words:
                    current.append(word)

                    backtrack(j)

                    current.pop()

        backtrack(0)
        return answer