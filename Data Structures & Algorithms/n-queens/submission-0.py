class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        current = []
        columns = set()
        west_diag = set()
        east_diag = set()

        def backtrack(i, n):
            if i == n:
                answer.append(current.copy())
                return
            for j in range(n):
                if j in columns or i - j in west_diag or i + j in east_diag:
                    continue

                # Place queen
                columns.add(j)
                west_diag.add(i - j)
                east_diag.add(i + j)
                current.append((i, j))

                # Recurse
                backtrack(i + 1, n)

                # Backtrack
                current.pop()
                columns.remove(j)
                west_diag.remove(i - j)
                east_diag.remove(i + j)

            return
        
        backtrack(0,n)

        boards = []
        for coordinates in answer:
            new_board = [["."] * n for _ in range(n)]

            for i, j in coordinates:
                new_board[i][j] = "Q"

            boards.append(
                ["".join(row) for row in new_board]
            )

        return boards


