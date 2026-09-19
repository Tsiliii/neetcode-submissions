class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        seen = set(nums)

        for x in nums:
            if x-1 not in seen:
                length = 1

                while x + length in seen:
                    length += 1
                answer = max(length, answer)

        return answer