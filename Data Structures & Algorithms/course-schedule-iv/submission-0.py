class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for a, b in prerequisites:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)

        seen = set()
        reachability = {}
        answer = [False] * len(queries)

        def dfs(node):
            if node in seen:
                return reachability[node]

            seen.add(node)
            reachability[node] = set()
            if node in adj:
                for neighbor in adj[node]:
                    reachability[node].add(neighbor)
                    reachability[node].update(dfs(neighbor))
            
            return reachability[node]

        for i,[x,y] in enumerate(queries):
            if y in dfs(x):
                answer[i] = True
        return answer
            