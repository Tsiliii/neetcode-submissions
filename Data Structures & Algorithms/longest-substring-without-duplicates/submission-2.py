class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 1
        answer = 1
        seen = {s[0]: 1}

        while(right < len(s)):
            character = s[right]
            if character not in seen:
                seen[character] = 0
            seen[character] += 1
            if seen[character] > 1:
                left_character = s[left]
                while(left_character != character):
                    seen[left_character] -= 1
                    left += 1
                    left_character = s[left]
                seen[left_character] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)
            right += 1



        return answer
            
