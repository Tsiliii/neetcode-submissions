class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = {}

        for x in nums:
            counts[x] = counts.get(x,0) + 1

        answer = []
        current = []

        def recursive():
            if len(current) == len(nums):
                answer.append(current.copy())
                return

            for x in counts:
                if counts[x] == 0:
                    continue

                current.append(x)
                counts[x] -= 1

                recursive()

                counts[x] += 1
                current.pop()
            
            return

        recursive()
        return answer