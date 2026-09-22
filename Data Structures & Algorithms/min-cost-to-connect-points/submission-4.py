class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0

        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance,i,j,))
        edges.sort()

        f = list(range(n))

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            
            f[rx] = ry
            return True

        index = 0
        answer = 0
        while(n > 1):
            distance, i, j = edges[index]
            if union(i,j):
                n -= 1
                answer += distance
            index += 1
        return answer
