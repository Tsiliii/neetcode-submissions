class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # n = len(nums)
        # answer = set()
        # for i in range(n-1):
        #     target = -1 * nums[i]
        #     seen = set()
        #     seen.add(target - nums[i + 1])
        #     for j in range(i+2, n):
        #         if nums[j] in seen:
        #             sorted_tuple = tuple(sorted([nums[i], target - nums[j], nums[j]]))
        #             answer.add(sorted_tuple)
        #         if target - nums[j] not in seen:
        #             seen.add(target - nums[j])
        # return [list(ans) for ans in answer]

        nums.sort()
        answers = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    answers.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k) and nums[j-1] == nums[j]:
                        j += 1
                    while(j < k) and nums[k+1] == nums[k]:
                        k -= 1
        return answers
                
