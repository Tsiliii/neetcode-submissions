import heapq
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        priority = []
        nodes = set()
        heapq.heapify(priority)
        dist = {}
        adj = {}
        for x,y,w in flights:
            if x not in adj:
                adj[x] = []
            adj[x].append((y,w))
            nodes.add(x)
            nodes.add(y)
        
        k = min(len(nodes), k)
        
        heapq.heappush(priority, (0, src, k+1))
        
        while priority:
            travel, node, stops = heapq.heappop(priority)
            if node == dst:
                return travel

            if node not in adj or stops < 0:
                continue

            for neighbor, w in adj[node]:
                neighbor_distance = w + travel
                if stops > 0 and ((neighbor, stops-1) not in dist or dist[(neighbor, stops-1)] > neighbor_distance):
                    dist[(neighbor, stops-1)] = neighbor_distance
                    heapq.heappush(priority, (neighbor_distance, neighbor, stops-1))
        
        return -1
