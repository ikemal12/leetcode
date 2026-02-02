class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first pass for prefix
        prefix = []
        prod = 1
        for num in nums:
            prefix.append(prod)
            prod *= num
            

        # second pass for suffix
        suffix = [-1] * len(nums)
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = prod
            prod *= nums[i]
            

        # final pass to compute products
        res = []
        for i in range(len(nums)):
            prod = prefix[i] * suffix[i]
            res.append(prod)
        return res















        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        prefix = []
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[i]
            prefix.append(prod)
        
        postfix = []
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod = prod * nums[i]
            postfix.append(prod)
        postfix = postfix[::-1]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res















        res = []
        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        """def getProduct(i):
            prod = 1
            for n in range(len(nums)):
                if n != i:
                    prod *= nums[n]
            return prod

        res = []
        for i in range(len(nums)):
            prod = getProduct(i)
            res.append(prod)
        return res"""