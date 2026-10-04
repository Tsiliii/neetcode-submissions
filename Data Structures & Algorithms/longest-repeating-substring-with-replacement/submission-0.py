class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        counts = {}
        left = 0
        right = 0
        answer = 0

        while right < len(s):
            
            # valid window
            while (right - left) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            
            counts[s[right]] = counts.get(s[right],0) + 1
            max_freq = max(max_freq, counts[s[right]])
            right += 1
            if (right - left) - max_freq <= k:
                answer = max(answer, right - left)

        return answer