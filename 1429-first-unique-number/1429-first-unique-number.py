class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.map = defaultdict(int)
        for n in nums:
            self.q.append(n)
            self.map[n] += 1

    def showFirstUnique(self) -> int:
        while self.q and self.map[self.q[0]] >= 2:
            self.q.popleft()
        if self.q: 
            return self.q[0]
        return -1


    def add(self, value: int) -> None:
        self.q.append(value)
        self.map[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)