class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return nums[i]
        #     seen.add(nums[i])

        slow = nums[0]
        fast = nums[nums[0]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow
        #     if nums[nums[i]] == i:
        #         return i
        #     else:
        #         nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        # return -1



























    # def findDuplicate(self, nums: List[int]) -> int:
#         slow = nums[nums[0]]
#         fast = nums[nums[nums[0]]]

#         while(slow!=fast):
#             slow = nums[slow]
#             fast = nums[nums[fast]]

#         slow = nums[0]
        
#         while(slow!=fast):
#             slow = nums[slow]
#             fast = nums[fast]

#         return slow