class Solution:
    def arrangeCoins(self, n: int) -> int:
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