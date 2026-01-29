class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n

        seen.add(cur)
        while cur != 1:
            sum = 0
            for digit in str(cur):
                sum += int(digit) ** 2

            if sum == 1:
                return True
            if sum in seen:
                return False
            seen.add(sum)
            cur = sum
        
        #[19, 81, ]
        
















        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
