class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens, odds = [], []
        for i, n in enumerate(nums):
            if i % 2:
                odds.append(n)
            else:
                evens.append(n)
        
        evens.sort()
        odds.sort(reverse=True)

        p1, p2 = 0, 0
        res = []
        while p1 < len(evens) and p2 < len(odds):
            res.append(evens[p1])
            res.append(odds[p2])
            p1 += 1
            p2 += 1
        if p1 == len(evens) - 1:
            res.append(evens[p1])
        return res


        