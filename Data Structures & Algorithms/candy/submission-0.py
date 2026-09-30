class Solution:
    def candy(self, ratings: List[int]) -> int:
        answer = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i - 1]:
                answer[i] = answer[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                answer[i] = max(answer[i], answer[i+1] + 1)

        # print(answer)
        return sum(answer)