class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list1 = m - 1
        list2 = n - 1
        i = n+m-1
        while list1 >= 0 and list2 >= 0:
            if nums1[list1] > nums2[list2]:
                nums1[i] = nums1[list1]
                list1 -= 1
            else:
                nums1[i] = nums2[list2]
                list2 -= 1
            i -= 1

        if list1 < 0:
            for i in range(list2+1):
                nums1[i] = nums2[i]

        return