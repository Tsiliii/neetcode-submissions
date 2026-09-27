class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # create heap with edges
        # set up union find to make sure that you do not connect the same component as you pop edges
        # while find(0,0) != find(n-1,m-1)
        # pop edge, keep weight as answer if not cycle union the two (or just union, since connected componenets union doesn't do anything)
        # return answer

        n, m = len(heights), len(heights[0])

        parent = list(range(n * m))
        size = [1] * (n * m)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)

            if rx == ry:
                return

            if size[rx] < size[ry]:
                rx, ry = ry, rx

            parent[ry] = rx
            size[rx] += size[ry]

        edges = []

        for i in range(n):
            for j in range(m):
                u = i * m + j

                if i + 1 < n:
                    v = (i + 1) * m + j
                    weight = abs(heights[i][j] - heights[i + 1][j])
                    edges.append((weight, u, v))

                if j + 1 < m:
                    v = i * m + j + 1
                    weight = abs(heights[i][j] - heights[i][j + 1])
                    edges.append((weight, u, v))

        edges.sort()

        start, end = 0, n * m - 1

        if start == end:
            return 0

        for weight, u, v in edges:
            union(u, v)

            if find(start) == find(end):
                return weight