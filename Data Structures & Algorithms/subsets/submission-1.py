class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # answer = [[]]
        # for x in nums:
        #     to_append = []
        #     for ans in answer:
        #         to_append.append(ans + [x])
        #     answer += to_append
        # return answer

        answer = []
        current = []

        def backtrack(index):
            if index == len(nums):
                answer.append(current.copy())
                return
            else:
                current.append(nums[index])
                backtrack(index + 1)
                current.pop()

                backtrack(index + 1)
                return
        
        backtrack(0)
        return answer
