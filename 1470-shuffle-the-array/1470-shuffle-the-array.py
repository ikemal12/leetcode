class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l, r = 0, n
        res = []
        while r < 2 * n:
            res.append(nums[l])
            res.append(nums[r])
            l, r = l + 1, r + 1
        return res

        """[2,5,1,3,4,7]
         l     r
        """