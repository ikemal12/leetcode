
class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n, mem):
            if n == 0: mem[n] = 0
            if n == 1: mem[n] = 1
            if n == 2: mem[n] = 2
            if mem[n] > 0: return mem[n]
            mem[n] = fib(n - 1, mem) + fib(n - 2, mem)
            return mem[n]
        return fib(n, [0] * (n + 1))

        [0, 1, 2, 3]

        """n = 1, f(n) = 1
        n =  2, f(n) = 2
        n = 3, f(n) = 3
        n = 4, f(4) = 5"""















        
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one








        def fib(x, store={}):
            if x == 1:
                return 1
            if x == 2:
                return 2
            if x in store:
                return store[x]
            store[x] = fib(x-1) + fib(x-2)
            return store[x]
        
        return fib(n)
            