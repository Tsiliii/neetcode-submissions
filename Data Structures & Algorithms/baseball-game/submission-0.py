class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for string in operations:
            if string == '+':
                record.append(record[-1] + record[-2])
            elif string == 'D':
                record.append(record[-1] * 2)
            elif string == 'C':
                record.pop()
            else:
                record.append(int(string))

        return sum(record)