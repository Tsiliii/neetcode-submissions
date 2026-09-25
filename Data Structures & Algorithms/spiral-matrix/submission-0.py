class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        bot, right = len(matrix) - 1, len(matrix[0]) - 1
        answer = []

        while top <= bot and left <= right:

            # Right
            for j in range(left, right + 1):
                answer.append(matrix[top][j])
            top += 1

            # Down
            for i in range(top, bot + 1):
                answer.append(matrix[i][right])
            right -= 1

            if top > bot or left > right:
                break

            # Left
            for j in range(right, left - 1, -1):
                answer.append(matrix[bot][j])
            bot -= 1

            # Up
            for i in range(bot, top - 1, -1):
                answer.append(matrix[i][left])
            left += 1

        return answer