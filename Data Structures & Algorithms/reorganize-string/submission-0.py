import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        heap = []
        for key, value in freq.items():
            heap.append([-1 * value, key])
        
        heapq.heapify(heap)
        answer = []
        while(heap):
                first_left, first_char = heapq.heappop(heap)
                answer.append(first_char)
                if not heap:
                    if first_left != -1:
                        return ""
                    else:
                        break
                second_left, second_char = heapq.heappop(heap)
                answer.append(second_char)
                if first_left < -1:
                    heapq.heappush(heap, [first_left+1, first_char])        
                if second_left < -1:
                    heapq.heappush(heap, [second_left+1, second_char])
        return "".join(answer)