class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


        """
        return ([x for x in nums if x % 2 == 0] +
                [x for x in nums if x % 2 == 1])"""


        """nums.sort(key=lambda x: x % 2)
        return nums"""