class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if nums[i] == 0:
                jump = i
            elif nums[i] > 0:
                jump = (i + nums[i]) % n
            else:
                jump = (i - abs(nums[i])) % n
            res[i] = nums[jump]
        return res
        