class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
        return

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimums or self.minimums[-1] >= val:
            self.minimums.append(val)
        return

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minimums[-1]:
            self.minimums.pop()
        return

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]
