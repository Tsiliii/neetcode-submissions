from math import factorial

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        current = []

        def recursive(index, n, k):
            # if (index > n+1) or k < 0:
            #     return
            if k == 0:
                answer.append(current.copy())
                return
            else:
                for i in range(index, n+1):
                    current.append(i)
                    recursive(i+1, n, k-1)
                    current.pop()
            return

        recursive(1,n,k)
        return answer
