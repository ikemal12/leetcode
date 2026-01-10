class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        res = self.stack2.pop()
        while self.stack2:
            val = self.stack2.pop()
            self.stack1.append(val)
        return res

    def peek(self) -> int:
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        res = self.stack2.pop()
        self.stack2.append(res)
        while self.stack2:
            val = self.stack2.pop()
            self.stack1.append(val)
        return res

    def empty(self) -> bool:
        if len(self.stack1):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()