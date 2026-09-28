class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        self.unsuccessful = set()
        self.success = False

        def backtrack(current, i, target):
            key = (current, i)
            if key in self.unsuccessful or self.success:
                return 

            if current == target:
                self.success = True
                return
            elif current > target or i == len(nums):
                self.unsuccessful.add(key)
                return
            else:
                backtrack(current + nums[i], i+1, target)
                if self.success:
                    return 
                backtrack(current, i+1, target)
                if self.success:
                    return 
                self.unsuccessful.add(key)
            
        backtrack(0, 0, target)
        return self.success

