class Solution:
    def fib(self, n: int) -> int:
        p1, p2 = 0, 1
        if n == p1 or n == p2:
            return n
        for i in range(n-1):
            tmp = p2
            p2 = p1 + p2
            p1 = tmp
        return p2

        """
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)"""

