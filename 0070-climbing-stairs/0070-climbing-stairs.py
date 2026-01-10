class Solution:
    def climbStairs(self, n: int) -> int:
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
            