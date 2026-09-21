class Solution:
    def dfs(self, course: int) -> int:
        if course in self.path:
            return False

        if course in self.seen:
            return True

        self.seen.add(course)
        self.path.add(course)
        for new_course in self.adj.get(course, []):
            if not self.dfs(new_course):
                return False
        self.path.remove(course)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = {}
        for a, b in prerequisites:
            if a not in self.adj:
                self.adj[a] = []
            self.adj[a].append(b)

        self.seen = set()
        for course in range(numCourses):
            self.path = set()
            if course not in self.seen and not self.dfs(course):
                return False
        return True
