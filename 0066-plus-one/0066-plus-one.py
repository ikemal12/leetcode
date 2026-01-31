class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        return [1] + digits
   

        """
        [9] -> [1, 0]
        [9, 9, 9] -> [1, 0, 0, 0]
        [1, 2, 9, 9] -> [1, 3, 0, 0]
        """