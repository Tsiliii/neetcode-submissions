class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = min(nums)
        min_so_far = max_so_far = nums[0]

        for i in range(1,len(nums)):
            x = nums[i]
            min_so_far, max_so_far = min(min_so_far * x, max_so_far * x, x), max(min_so_far * x, max_so_far * x, x)

            answer = max(answer, min_so_far, max_so_far)

        return answer

        # prev = left = right = -1
        # i = 0
        # answer = max(nums)

        # while (True):

        #     # compute the best solution
        #     if i == n or nums[i] == 0:
        #         if left == right == prev:
        #             current = 1
        #             for index in range(prev+1, i):
        #                 current *= nums[index]

        #         elif right == prev:
        #             current = 1
        #             for index in range(prev+1, i):
        #                 if index == left:
        #                     answer = max(answer, current)
        #                     current = 1
        #                 else:
        #                     current *= nums[index]
                
        #         else:
        #             left_current = 1
        #             right_current = 1
        #             for index in range(prev+1, i):
        #                 if index < right:
        #                     left_current *= nums[i]
        #                 if index > left:
        #                     right_current *= nums[i]

        #         answer = max(answer, current)
        #         prev = left = right = i

        #     # if left == right = prev
        #     # 
        #     elif nums[i] < 0:
        #         if left == right:
        #             left = i
        #         else:
        #             right = i

        #     i += 1


