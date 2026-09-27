class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        answer = []
        current = []
        i = 0

        def recursive(index, target):
            if target == 0:
                answer.append(current.copy())
                # current.pop()
                return
            elif target < 0 or index == len(candidates):
                # current.pop()
                return
            else:
                # check for the next
                current.append(candidates[index])
                recursive(index+1, target - candidates[index])
                current.pop()
                for i in range(index+1, len(candidates)):
                    if candidates[i] != candidates[i - 1]:
                        current.append(candidates[i])
                        recursive(i+1, target - candidates[i])
                        current.pop()
                return

        recursive(0,target)
        return answer

