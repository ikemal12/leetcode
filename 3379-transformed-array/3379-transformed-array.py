class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = nums[i]
            elif nums[i] > 0:
                if i + nums[i] < n:
                    res[i] = nums[i + nums[i]]
                else:
                    jump = ((i + nums[i]) % n) 
                    res[i] = nums[jump]
            else:
                jump = (i - abs(nums[i])) % n
                res[i] = nums[jump]
        return res
        