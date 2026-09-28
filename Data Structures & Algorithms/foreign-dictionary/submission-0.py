class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # compare each word with the next.
        # the first letter they differ dictates the information we know
        # if 'a' < 'b' we add edge b -> a
        # then we run dfs on each node (that has at least one edge), and when we are done exploring said node we add it to the answer

        # Initialize graph with every distinct character
        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()

        # Build ordering constraints
        for i in range(len(words) - 1):
            left, right = words[i], words[i + 1]

            # Invalid prefix case
            if len(left) > len(right) and left.startswith(right):
                return ""

            # Find the first differing character
            for j in range(min(len(left), len(right))):
                if left[j] != right[j]:
                    # right[j] depends on left[j]
                    adj[right[j]].add(left[j])
                    break

        # DFS topological sorting
        seen = set()
        path = set()
        answer = []

        def dfs(char):
            if char in path:
                return False

            if char in seen:
                return True

            path.add(char)

            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False

            path.remove(char)
            seen.add(char)
            answer.append(char)

            return True

        # Process all characters, including isolated ones
        for char in adj:
            if char not in seen:
                if not dfs(char):
                    return ""

        return "".join(answer)