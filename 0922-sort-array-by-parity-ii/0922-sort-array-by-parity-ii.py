class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = 1
        for r in range(0, len(nums), 2):
            if nums[r] % 2:
                while nums[l] % 2:
                    l += 2
                nums[l], nums[r] = nums[r], nums[l]
        return nums