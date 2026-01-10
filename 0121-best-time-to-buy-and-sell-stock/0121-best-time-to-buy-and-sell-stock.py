class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP















        l, r = 0, 1
        res = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                res = max(res, profit)
            else:
                l = r
            r += 1

        return res














        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        """
        res = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                res = max(res, profit)
        return res"""


