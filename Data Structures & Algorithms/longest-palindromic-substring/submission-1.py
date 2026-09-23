class Solution:
    def check(self, left, right, s):
        if s[left] != s[right]:
            return (left+1,right-1)
        elif left == 0 or right == len(s)-1:
            return (left, right)
        else:
            return self.check(left-1, right+1, s)
    
    def replace(self, left, right, answer_left, answer_right):
        if (right - left) > answer_right - answer_left:
            return left, right 
        return answer_left, answer_right

    def longestPalindrome(self, s: str) -> str:
        answer_left, answer_right = 0, 0
        for i in range(0,len(s)-1):
            left, right = self.check(i,i+1,s)
            answer_left, answer_right = self.replace(left, right, answer_left, answer_right)
            left, right = self.check(i,i,s)

            answer_left, answer_right = self.replace(left, right, answer_left, answer_right)
        return s[answer_left: answer_right + 1]
