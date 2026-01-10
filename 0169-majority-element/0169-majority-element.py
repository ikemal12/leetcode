class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # optimal solution with O(1) space
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res


        counts = {}
        n = len(nums)
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for key, count in counts.items():
            if count > n / 2:
                return key














        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res


        # O(n) space with hashmap
        """count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res"""