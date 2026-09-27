class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]

        for x in nums:
            to_add = []

            for sub in subsets:
                to_add.append(sub + [x])

            subsets.extend(to_add)

        print(subsets)
        answer = 0
        
        for sub in subsets:
            partial_sum = 0
            for x in sub:
                partial_sum ^= x
            answer += partial_sum
        return answer