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
            self.push(val)
            #if i == n - 1:
                #self.topOfStack = val
        return self.q1.popleft()


        """while self.q1 and len(self.q1) > 1:
            val = self.q1.popleft()
            self.q2.append(val)
            self.topofStack = val
        res = self.q1.popleft()

        while self.q2:
            val = self.q2.popleft()
            self.q1.append(val)
        return res"""

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