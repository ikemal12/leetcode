class Solution:
    def isBalanced(self, num: str) -> bool:
        even = odd = 0

        for i in range(len(num)):
            if i % 2:
                odd += int(num[i])
            else:
                even += int(num[i])

        return even == odd