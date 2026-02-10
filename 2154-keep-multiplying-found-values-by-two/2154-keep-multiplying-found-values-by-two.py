class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for num in nums:
            if num == original:
                original *= 2
        return original


        """
        o = original
        while True:
            found = False
            for i in range(len(nums)):
                if nums[i] == o:
                    o = o * 2
                    found = True
            if found:
                continue
            else:
                break
        return o"""
            