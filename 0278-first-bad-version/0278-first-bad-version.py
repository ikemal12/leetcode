# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m) and not isBadVersion(m-1):
                return m
            elif isBadVersion(m) and isBadVersion(m-1):
                r = m - 1
            elif not isBadVersion(m) and not isBadVersion(m-1):
                l = m + 1
        
