class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d_to_c = {
            "2": "abc",
            "3": "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        answer = [""]
        for d in digits:
            new_answer = []
            for character in d_to_c[d]:
                for ans in answer:
                    new_answer.append(ans + character)
            answer = new_answer
        return answer