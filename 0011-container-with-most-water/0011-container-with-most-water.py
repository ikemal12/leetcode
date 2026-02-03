class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0

        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[r], height[l])
            maxA = max(maxA, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxA

        """
        maxA = 0 
        [1,8,6,2,5,4,8,3,7]
         l               r
        """















        l, r = 0, len(height) - 1
        maxA = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxA = max(maxA, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxA















        l, r = 0, len(height) - 1
        res = 0
        while l <= r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res