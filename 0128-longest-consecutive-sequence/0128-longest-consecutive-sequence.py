class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)

        for num in s:
            if num - 1 not in s:
                length = 0
                while num + length in s:
                    length += 1
                longest = max(longest, length)
        return longest

        """
        if not nums: return 0
        nums.sort()
        res = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 1

        return max(res, count)"""














        if not nums:
            return 0
        nums.sort()
        res = 0
        curr = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] - nums[i] == 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
        res = max(res, curr)
        return res