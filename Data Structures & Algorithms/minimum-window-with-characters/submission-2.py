class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def index(char):
            if char.islower():
                return ord(char) - ord('a')
            return ord(char) - ord('A') + 26

        def compare(l1,l2):
            for i in range(52):
                if l1[i] > l2[i]:
                    return False
            return True

        required = [0] * 52
        window = [0] * 52

        for char in t:
            required[index(char)] += 1

        best_start = 0
        best_length = float("inf")
        left = 0

        for right, char in enumerate(s):
            window[index(char)] += 1

            while compare(required, window):
                length = right - left + 1

                if length < best_length:
                    best_length = length
                    best_start = left

                window[index(s[left])] -= 1
                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]