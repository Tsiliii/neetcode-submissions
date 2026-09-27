from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)

        if "0000" in seen:
            return -1

        queue = deque([("0000", 0)])
        seen.add("0000")

        while queue:
            combination, moves = queue.popleft()

            if combination == target:
                return moves

            for i in range(4):
                digit = int(combination[i])

                for delta in (-1, 1):
                    new_digit = (digit + delta) % 10

                    neighbor = (
                        combination[:i]
                        + str(new_digit)
                        + combination[i + 1:]
                    )

                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, moves + 1))

        return -1