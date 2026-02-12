class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(n):
            cur = 0
            for r in range(l, n):
                cur += arr[r]
                res += cur if (r - l + 1) % 2 == 1 else 0
        return res



        """ # O(n^3)
        n = len(arr)
        res = 0

        for l in range(n):
            for r in range(l, n):
                if (r - l + 1) % 2:
                    cur = 0
                    for i in range(l, r + 1):
                        cur += arr[i]
                    res += cur
        return res"""