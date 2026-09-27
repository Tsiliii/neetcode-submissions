class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # answer = [[nums[0]]]
        # for x in nums[1:]:
        #     new_answers = []
        #     for perm in answer:
        #         for i in range(len(perm)+1):
        #             new_answers.append(perm[i:]+ [x] + perm[:i])
        #     answer = new_answers
        # return answer
        answer = []
        numbers = set(nums)
        current = []

        def backtrack():
            if len(current) == len(nums):
                answer.append(current.copy())
                return
            else:
                for x in nums:
                    if x in numbers:
                        current.append(x)
                        numbers.remove(x)
                        backtrack()
                        current.pop()
                        numbers.add(x)

                return
        
        backtrack()
        return answer
