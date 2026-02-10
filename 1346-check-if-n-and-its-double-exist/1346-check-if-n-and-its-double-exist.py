class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in range(len(arr)):
            if (arr[i] * 2) in seen or (arr[i]/2) in seen:
                return True
            seen.add(arr[i])
        return False


        
        """
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True
        return False"""