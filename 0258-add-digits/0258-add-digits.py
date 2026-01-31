class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while res > 9:
            sum = 0
            while res:
                sum += (res % 10)
                res = res // 10
            res = sum
        return res

        
        """423% 10
        = 3

        423 // 10 = 42

        42 % 10 = 2

        42 // 10 = 4

        4 % 10 = 0"""

 