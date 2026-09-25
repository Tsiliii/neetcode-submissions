class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        
        row, columns = False, False
        for j in range(m):
            row = row or (matrix[0][j] == 0)
        for i in range(n):
            columns = columns or (matrix[i][0] == 0)
            
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(1,m):
                    matrix[i][j] = 0

        for j in range(1,m):
            if matrix[0][j] == 0:
                for i in range(1,n):
                    matrix[i][j] = 0

        if row:
            for j in range(m):
                matrix[0][j] = 0
        if columns:
            for i in range(n):
                matrix[i][0] = 0

        return 