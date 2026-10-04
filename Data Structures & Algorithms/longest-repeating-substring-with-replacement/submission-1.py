class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        counts = {}
        left = 0
        answer = 0

        for right in range(0, len(s)):
            counts[s[right]] = counts.get(s[right],0) + 1
            max_freq = max(max_freq, counts[s[right]])
            
            # valid window
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)

        return answer