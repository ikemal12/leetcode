class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9

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

 