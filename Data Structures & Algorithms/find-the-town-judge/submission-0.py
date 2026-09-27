class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge_edges = [[set(), set()] for _ in range(n+1)]

        for a, b in trust:
            judge_edges[a][0].add(b)
            judge_edges[b][1].add(a)

        for index, [me,other] in enumerate(judge_edges):
            if len(other) == n-1:
                if len(me) == 0:
                    return index
                else:
                    return -1

        return -1