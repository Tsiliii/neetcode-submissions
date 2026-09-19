class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequencies_array = [[] for _ in range(n+1)]
        frequencies_dictionary = {}
        for number in nums:
            if number not in frequencies_dictionary:
                frequencies_dictionary[number] = 0
            frequencies_dictionary[number] += 1
        
        for key, value in frequencies_dictionary.items():
            frequencies_array[value].append(key)

        i = n
        answer = []
        while(k > 0):
            if len(frequencies_array[i]) > 0:
                answer += frequencies_array[i]
                k -= len(frequencies_array[i])
            i -= 1
        return answer
