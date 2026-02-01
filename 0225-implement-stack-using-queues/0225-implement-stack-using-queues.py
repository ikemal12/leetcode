class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.topofStack = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topofStack = x

    def pop(self) -> int:
        n = len(self.q1)-1
        for i in range(n):
            val = self.q1.popleft()
            self.q1.append(val)
            if i == n - 1:
                self.topofStack = val
        return self.q1.popleft()

    def top(self) -> int:
        return self.topofStack

    def empty(self) -> bool:
        return len(self.q1) == 0

"""
    [2, 3, 1]"""


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()