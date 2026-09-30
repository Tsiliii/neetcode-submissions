class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        answer = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last[char])

            if i == end:
                answer.append(end-start+1)
                start = end + 1

        return answer
        # frequencies = {}
        # for char in s:
        #     frequencies[char] = 1 + frequencies.get(char,0)

        # answer = []
        # counter = 0
        # waiting = set()

        # for char in s:
        #     waiting.add(char)
        #     counter += 1

        #     if frequencies[char] == 1 and len(waiting) == 1:
        #         answer.append(counter)
        #         counter = 0
        #         waiting.remove(char)
        #     else:
        #         frequencies[char] -= 1
        #         if frequencies[char] == 0:
        #             waiting.remove(char)

        # return answer 