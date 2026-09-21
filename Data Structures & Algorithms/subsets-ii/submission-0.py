class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = [[]]
        
        i = 0
        while (i < len(nums)):
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            to_combine = [[nums[i]] * k for k in range(1, j-i+1)] 

            new_answers = []
            for old in answer:
                for comb in to_combine:
                    new_answers.append(old + comb)
            
            answer.extend(new_answers)
            i = j
        return answer