class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])

        answer = [[0] * n for _ in range(m)]
        
        for i in range(0, n):
            for j in range(0, m):
                answer[j][i] = matrix[i][j]

        return answer