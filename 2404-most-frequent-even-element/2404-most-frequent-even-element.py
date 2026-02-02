class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num % 2 == 0:
                counts[num] = 1 + counts.get(num, 0)
        
        res = maxCount = -1
        for num, count in counts.items():
            if count == maxCount:
                res = min(res, num)
            elif count > maxCount:
                maxCount = count
                res = num
        return res