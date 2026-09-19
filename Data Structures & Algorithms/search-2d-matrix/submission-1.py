class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left = 0
        right = n * m - 1

        while(left < right):
            mid = (left + right) // 2
            i = mid // m
            j = mid % m
            
            if target <= matrix[i][j]:
                right = mid
            else:
                left = mid + 1

        i, j = left // m, left % m
        return (left == n*m or matrix[i][j] == target)