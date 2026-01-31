class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n] #store x, y

        j = 2*n - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j-1] = x
            j -= 2
        return nums

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