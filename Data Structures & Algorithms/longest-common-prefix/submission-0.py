class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(1, len(strs)):
            endpoint = min(len(word),len(strs[i]))
            j = 0
            while j < endpoint and word[j] == strs[i][j]:
                j += 1

            word = word[:j]

        return word