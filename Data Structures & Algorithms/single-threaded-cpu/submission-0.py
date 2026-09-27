class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(x,y,i) for i, [x,y] in enumerate(tasks)]
        tasks.sort()

        answer = [tasks[0][2]]
        t = tasks[0][0] + tasks[0][1]

        index = 1
        n = len(tasks)
        heap = []
        heapq.heapify(heap)

        while(index < n or heap):
            while(index < n and tasks[index][0] <= t):
                heapq.heappush(heap,[tasks[index][1],tasks[index][2]])
                index += 1
            
            if not heap:
                t = tasks[index][0]
                continue
            process, element = heapq.heappop(heap)
            t += process
            answer.append(element)
        return answer
