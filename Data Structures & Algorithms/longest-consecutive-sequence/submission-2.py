class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f = {}
        size = {}
        for x in nums:
            f[x] = x
            size[x] = 1

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx!= ry:
                f[rx] = ry
                size[ry] += size[rx]

        for x in nums:
            if x-1 in f:
                union(x, x-1)
            if x+1 in f:
                union(x, x+1)

        return max(size.values())