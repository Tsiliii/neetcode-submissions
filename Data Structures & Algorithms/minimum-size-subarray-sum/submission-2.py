class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        answer = n + 1
        left = 0
        right = 0
        current_sum = 0
        length = 0

        while(right <= n):
            if current_sum == 0 or current_sum < target:
                if right == n:
                    break
                current_sum += nums[right]
                right += 1
                length += 1
            else:
                answer = min(answer, length)
                current_sum -= nums[left]
                left += 1
                length -= 1

        return answer if answer != n+1 else 0