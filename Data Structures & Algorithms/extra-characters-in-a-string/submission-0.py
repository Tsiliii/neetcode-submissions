class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)
        memo = {len(s) : 0}
        self.answer = len(s) + 1

        def backtrack(index:int, memo:dict) -> int:
            if index in memo:
                return memo[index]
            
            best = 1 + backtrack(index + 1, memo)

            # Option 2: Match a dictionary word
            for j in range(index + 1, len(s) + 1):
                if s[index:j] in dict_set:
                    best = min(best, backtrack(j, memo))
            
            memo[index] = best
            return best

        return backtrack(0,memo)