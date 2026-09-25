class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        answer = 0
        # if nums[0] == k:
        #     answer += 1
        # freq[nums[0]] = 1
        prefix = 0

        for x in nums:
            prefix += x
            
            answer += freq.get(prefix-k, 0)

            freq[prefix] = freq.get(prefix, 0) + 1

        return answer
