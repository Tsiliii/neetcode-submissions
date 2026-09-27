class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        side = sum(matchsticks) // 4
        available = {}
        for x in matchsticks:
            available[x] = available.get(x,0) + 1
        answer = False

        def backtrack(current_side, used):
            # if answer == True:
            #     return 
            if current_side < 0 or current_side > 0 and used == 0:
                return False

            if current_side == 0:
                if used == 0:
                    return  True          

                current_side = side
            answer = False
            for x in available.keys():
                if available[x] == 0:
                    continue
                available[x] -= 1
                if backtrack(current_side - x, used - 1):
                    return True
                available[x] += 1
            return False
        
        return backtrack(side, len(matchsticks))
