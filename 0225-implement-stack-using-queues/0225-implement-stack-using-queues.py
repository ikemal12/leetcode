class MyStack:

    def __init__(self):
        self.q1, self.q2 = collections.deque(), collections.deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        """[]
        [1, 2]"""
        while self.q1 and len(self.q1) > 1:
            val = self.q1.popleft()
            self.q2.append(val)
        res = self.q1.popleft()

        while self.q2:
            val = self.q2.popleft()
            self.q1.append(val)
        return res

    def top(self) -> int:
        while self.q1 and len(self.q1) > 1:
            val = self.q1.popleft()
            self.q2.append(val)
        res = self.q1.popleft()
        while self.q2:
            val = self.q2.popleft()
            self.q1.append(val)
        self.q1.append(res)
        return res

    def empty(self) -> bool:
        return False if len(self.q1) else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()