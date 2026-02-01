class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first, second = cost[n - 1], 0

        for i in range(n - 2, -1, -1):
            tmp = first
            first = cost[i] + min(first, second)
            second = tmp
        return min(first, second)

        """
        n = len(cost)
        dp = [0] * (n + 1)
        dp[n] = 0
        dp[n - 1] = cost[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])"""


        """
        cost = [1,100,1,1,1,100,1,1,100,1] 0
                                     

        dp = [6,105,5,5,4,102,3,2,100,1]
              i
        """













        N = len(cost)
        cache = [-1] * N

        def dfs(i):
            if i >= N:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]
        
        return min(dfs(0), dfs(1))