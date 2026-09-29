class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        answer = 1
        current = 1
        increasing = True

        for i in range(1,len(arr)):
            if increasing:
                if arr[i] > arr[i-1]:
                    current +=1
                    increasing = False
                elif arr[i] < arr[i-1]:
                    current = 2
                    increasing = True
                else:
                    current = 1
                    increasing = True
            else:
                if arr[i] < arr[i-1]:
                    current += 1
                    increasing = True
                elif arr[i] > arr[i-1]:
                    current = 2
                    increasing = False
                else:
                    current = 1
                    increasing = True

            answer = max(answer, current)
        return answer