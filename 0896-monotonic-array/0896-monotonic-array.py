class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            elif nums[i] < nums[i + 1]:
                decreasing = False

        return increasing or decreasing



        """
        if nums[0] < nums[-1]:
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
        else:
            for i in range(1, len(nums)):
                if nums[i - 1] < nums[i]:
                    return False
        return True"""

