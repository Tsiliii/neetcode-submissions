class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,2,4,5,6,7,8,9,10]
        # [1,2,3,4]

        # nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        left = 0
        right = n

        while True:
            mid = (left + right) // 2
            other_mid = (n + m + 1) // 2 - mid

            low1 = nums1[mid - 1] if mid > 0 else float("-inf")
            high1 = nums1[mid] if mid < n else float("inf")
            low2 = nums2[other_mid - 1] if other_mid > 0 else float("-inf")
            high2 = nums2[other_mid] if other_mid < m else float("inf")
            # low1, high1, low2, high2 = nums1[mid-1], nums1[mid], nums2[other_mid-1], nums2[other_mid]
            # now we have nums1[mid] and nums[2][other_mid].
            # the partition is correct if both are less than their counterparts, e.g.
            if low1 <= high2 and low2 <= high1:
                break

            # when do i move the small partition to the right?
            elif low1 > high2:
                right = mid - 1
            else:
                left = mid + 1

        if (n + m) % 2:
            return max(low1, low2)

        return (max(low1, low2) + min(high1, high2)) / 2