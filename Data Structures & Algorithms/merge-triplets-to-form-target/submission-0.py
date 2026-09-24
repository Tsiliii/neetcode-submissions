class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        left = mid = right = False
        for x, y, z in triplets:
            if x == target[0] and y <= target[1] and z <= target[2]:
                left = True
            if y == target[1] and x <= target[0] and z <= target[2]:
                mid = True
            if z == target[2] and x <= target[0] and y <= target[1]:
                right = True
            if left == mid == right == True:
                return True
        return False

