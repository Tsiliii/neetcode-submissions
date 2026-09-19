class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left = 0
        right = n * m 

        while(left < right):
            mid = (left + right) // 2
            i = mid // m
            j = mid % m
            
            if target <= matrix[i][j]:
                right = mid
            else:
                left = mid + 1

        if left == n * m:
            return False
        i, j = left // m, left % m
        return matrix[i][j] == target