class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for x in nums:
            to_append = []
            for ans in answer:
                to_append.append(ans + [x])
            answer += to_append
        return answer