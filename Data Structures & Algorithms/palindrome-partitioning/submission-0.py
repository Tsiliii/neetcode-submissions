class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        current = []
        
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True



        def backtrack(index):
            if index == len(s):
                answer.append(current.copy())
                return 

            for i in range(index, len(s)):
                if is_palindrome(s,index, i):
                    current.append(s[index:i+1])
                    backtrack(i+1)
                    current.pop()
            return
        
        backtrack(0)
        return answer
