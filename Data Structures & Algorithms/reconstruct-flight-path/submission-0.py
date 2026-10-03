class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(city):
            if city not in graph:
                route.append(city)
                return 

            while graph[city]:
                nxt = heapq.heappop(graph[city])
                dfs(nxt)

            route.append(city)

        dfs('JFK')
        return route[::-1]