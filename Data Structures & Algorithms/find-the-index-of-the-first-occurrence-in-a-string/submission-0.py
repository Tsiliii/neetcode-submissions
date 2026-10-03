class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        lps = [0] * m
        lps[0] = 0
        prev = 0
        j = 1

        while(j < m):
            if needle[prev] == needle[j]:
                lps[j] = prev + 1
                prev += 1
                j += 1
            elif prev == 0:
                lps[j] = 0
                j += 1
            else:
                prev = lps[prev-1]


        i = 0
        j = 0
        while(i < len(haystack)):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == m:
                return i - m
        return -1


