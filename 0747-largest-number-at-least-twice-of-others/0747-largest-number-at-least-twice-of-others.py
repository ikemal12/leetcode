class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, maxIdx = 0, 0
        for i, n in enumerate(nums):
            if n > largest:
                largest = n
                maxIdx = i
        
        for i in range(len(nums)):
            if i != maxIdx and nums[i] * 2 > largest:
                return -1
        return maxIdx

