class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
        res = 0
        for n in nums:
            res ^= n
        return res














        res = 0
        for n in nums:
            res = res ^ n
        return res














        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)
        return hashset.pop()

        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res