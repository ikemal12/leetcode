class Solution:
    def fib(self, n: int) -> int:
        p1, p2 = 0, 1
        for i in range(n):
            p1, p2 = p2, p1+p2
        return p1

        """
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)"""

