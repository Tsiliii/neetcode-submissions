class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while(i < j):
            score = numbers[i] + numbers[j]
            if score > target:
                j -= 1
            elif score < target:
                i += 1
            else:
                return [i+1,j+1]
        return 
