class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for i in range(num):
                if (i | (i + 1)) == num:
                    ans.append(i)
                    break
                if i == num - 1:
                    ans.append(-1)
        return ans        

        """
        00100     
        00101
        00101


        0011
        0100
        0111
        """


