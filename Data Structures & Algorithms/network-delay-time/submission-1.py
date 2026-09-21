import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {}
        adj = {}
        for u, v, t in times:
            if u not in adj:
                adj[u] = []
            adj[u].append([v,t])
        for u in range(1,n+1):
            dist[u] = math.inf
        
        priority = [[0,k]]
        dist[k] = 0
        heapq.heapify(priority)

        while(priority):
            time, node = heapq.heappop(priority)
            if time > dist[node]:
                continue
            if node in adj:
                for next_node, t in adj[node]:
                    next_time = time + t
                    if next_time < dist[next_node]:
                        dist[next_node] = next_time
                        heapq.heappush(priority, [next_time, next_node])
        answer = max(dist.values())
        return answer if answer != math.inf else -1