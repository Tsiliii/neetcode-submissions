class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def condition(target: int, nums: List[int], k: int) -> bool:
            current = 0

            for x in nums:
                current += x
                if current > target:
                    current = x
                    k -= 1
                    
            return k > 0

        left = max(nums)
        right = sum(nums)

        while(left < right):
            mid = (left + right) //2

            if condition(mid, nums, k):
                right = mid
            else:
                left = mid + 1
        
        return left



        # def condition(mid:int, nums: List[int], k: int) -> bool:
        #     current = 0

        #     for x in nums:
        #         current += x
        #         if current > mid:
        #             k -= 1
        #             current = x
        #     return k > 0

        # # binary search on the answer.
        # left = max(nums)
        # right = sum(nums)

        # while(left < right):
        #     mid = (left + right) //2

        #     if condition(mid, nums, k):
        #         right = mid 
        #     else:
        #         left = mid + 1
        
        # return left