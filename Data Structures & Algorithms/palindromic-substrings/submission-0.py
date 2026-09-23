class Solution:
    def check(self, left, right, s: str) -> int:
        if left < 0 or right > len(s) - 1 or s[left] != s[right] :
            return 0
        elif left == 0 or right == len(s)-1:
            return 1
        else:
            return 1 + self.check(left-1, right+1, s)
    
    def replace(self, left, right, answer_left, answer_right):
        if (right - left) > answer_right - answer_left:
            return left, right 
        return answer_left, answer_right

    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(0,len(s)):
            answer += self.check(i,i+1,s) 
            # answer_left, answer_right = self.replace(left, right, answer_left, answer_right)
            
            answer += self.check(i,i,s)
            # answer_left, answer_right = self.replace(left, right, answer_left, answer_right)
        return answer