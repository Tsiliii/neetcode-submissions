class Solution:
    def totalNQueens(self, n: int) -> int:
        self.answer = 0
        current = []
        columns = set()
        west_diag = set()
        east_diag = set()

        def backtrack(i):
            if i == n:
                self.answer += 1
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
                backtrack(i + 1)

                # Backtrack
                current.pop()
                columns.remove(j)
                west_diag.remove(i - j)
                east_diag.remove(i + j)

            return
        
        backtrack(0)

        return self.answer

        