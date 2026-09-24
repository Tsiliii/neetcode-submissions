class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frequencies = {}
        for char in s:
            frequencies[char] = 1 + frequencies.get(char,0)

        answer = []
        counter = 0
        waiting = set()

        for char in s:
            waiting.add(char)
            counter += 1

            if frequencies[char] == 1 and len(waiting) == 1:
                answer.append(counter)
                counter = 0
                waiting.remove(char)
            else:
                frequencies[char] -= 1
                if frequencies[char] == 0:
                    waiting.remove(char)

        return answer 