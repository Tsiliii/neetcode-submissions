class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        answer = [nums[0]]
        n = len(nums)

        for i in range(1,n):
            x = nums[i]

            left = 0
            right = len(answer)
            while(left < right):
                mid = (left + right) // 2

                if answer[mid] >= x:
                    right = mid 
                else:
                    left = mid + 1
            
            if left == len(answer):
                answer.append(x)
            else:
                answer[left] = x
        
        return len(answer)
        