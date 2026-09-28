class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        small, medium, large = 0, 1, 1
        for _ in range(n-2):
            T = small + medium + large
            small, medium, large = medium, large, T

        return T