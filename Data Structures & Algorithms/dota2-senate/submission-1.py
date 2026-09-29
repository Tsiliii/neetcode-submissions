class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        out = set()

        R = 0
        D = 0

        radiant = senate.count("R")
        dire = senate.count("D")

        i = 0

        while radiant > 0 and dire > 0:

            if i not in out:

                if senate[i] == "R":
                    if R > 0:
                        R -= 1
                        radiant -= 1
                        out.add(i)
                    else:
                        D += 1

                else:
                    if D > 0:
                        D -= 1
                        dire -= 1
                        out.add(i)
                    else:
                        R += 1

            i = (i + 1) % n

        return "Radiant" if radiant > 0 else "Dire"
