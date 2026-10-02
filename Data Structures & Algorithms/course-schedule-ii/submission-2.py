class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for a, b in prerequisites:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)

        path = set()
        seen = set()
        answer = []

        def dfs(node: int, path: set, seen: set, adj: dict) -> bool:
            if node in path:
                return False
            elif node in seen:
                return True
            
            path.add(node)
            for neighbor in adj.get(node, []):
                if not dfs(neighbor, path, seen, adj):
                    return False
            path.remove(node)

            seen.add(node)

            answer.append(node)

            return True
        
        for i in range(numCourses):
            if i not in seen:
                if not dfs(i, path, seen, adj):
                    return []
        return answer
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     adj = {}
    #     for a, b in prerequisites:
    #         if a not in adj:
    #             adj[a] = []
    #         adj[a].append(b)

    #     path = set()
    #     seen = set()
    #     answer = []

    #     def dfs(node):

    #         if node in path:
    #             return False

    #         if node in seen:
    #             return True
            
    #         path.add(node)
    #         if node in adj:
    #             for neighbor in adj[node]:
    #                 if not dfs(neighbor):
    #                     return False
                    
    #         path.remove(node)
    #         seen.add(node)
    #         answer.append(node)
    #         return True

    #     for x in range(0,numCourses):
    #         if x not in seen and not dfs(x):
    #             return []
    #     return answer
        