class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n 
        while l <= r:
            m = (l + r) // 2
            coins = m*(m+1) // 2
            if coins == n:
                return m
            elif n < coins:
                r = m - 1
            else:
                l = m + 1
        return r

        """
        [1, 2, 3, 4, 5, 6, 7, 8]
               r 
                  l  
        """



        count = 1
        while n >= 0:
            n = n - count
            if n < 0:
                break
            count += 1
        return count - 1














        l, r = 0, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
        return res