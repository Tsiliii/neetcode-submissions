class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        path = [i.replace("/", "") for i in path]
        stack = []

        for i in path:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)