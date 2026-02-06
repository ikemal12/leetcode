class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                res[nums1Idx[val]] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res


        """
        nums1 = [4,1,2], nums2 = [1,3,4,2]
        res = [1]
        """


        """
        res = []
        for i in range(len(nums1)):
            start = 0
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    start = j
            if start == len(nums2) - 1:
                res.append(-1)
                continue

            found = False
            for k in range(start + 1, len(nums2)):
                if nums2[k] > nums1[i]:
                    res.append(nums2[k])
                    found = True
                    break
            
            if not found: res.append(-1)
        return res"""


