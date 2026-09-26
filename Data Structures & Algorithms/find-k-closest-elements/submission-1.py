class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n

        while(left < right):
            mid = (left + right) //2

            if arr[mid] >= x:
                right = mid
            else:
                left = mid+1

        # left is the first index >= x
        if left == n or (left > 0 and arr[left] - x >= x - arr[left -1]):
            left -= 1

        # if k == 1:
        #     return arr[left]
        
        right = left + 1
        left -= 1
        k -= 1

        while k > 0:
            if left < 0:
                right += 1
            elif right > n - 1:
                left -= 1
            elif arr[right] - x >= x - arr[left]:
                left -= 1
            else:
                right += 1
            k -= 1
        
        return arr[left+1:right]
            

        
