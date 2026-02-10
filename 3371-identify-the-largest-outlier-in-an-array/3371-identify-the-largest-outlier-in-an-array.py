class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        counts = collections.Counter(nums)
        outlier = float("-inf")

        for num in nums:
            counts[num] -= 1
            totalSum -= num
            if (totalSum % 2 == 0 and counts[totalSum // 2] > 0):
                outlier = max(outlier, num)
            counts[num] += 1
            totalSum += num
        return outlier
        



        """
        [1,1,1,1,1,5,5]
        """