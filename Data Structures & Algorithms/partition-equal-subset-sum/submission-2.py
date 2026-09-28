class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        if target in nums:
            return True

        compute = {nums[0]}
        for x in nums[1:]:
            to_add = set()
            for e in compute:
                if e + x == target:
                    return True
                elif e+x < target:
                    to_add.add(e+x)
            compute.update(to_add)
        return False

        # self.unsuccessful = set()
        # self.success = False

        # def backtrack(current, i, target):
        #     key = (current, i)
        #     if key in self.unsuccessful or self.success:
        #         return 

        #     if current == target:
        #         self.success = True
        #         return
        #     elif current > target or i == len(nums):
        #         self.unsuccessful.add(key)
        #         return
        #     else:
        #         backtrack(current + nums[i], i+1, target)
        #         if self.success:
        #             return 
        #         backtrack(current, i+1, target)
        #         if self.success:
        #             return 
        #         self.unsuccessful.add(key)
            
        # backtrack(0, 0, target)
        # return self.success

