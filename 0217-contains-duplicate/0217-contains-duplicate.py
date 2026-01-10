class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
















        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

















        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False














        map = set()
        for num in nums:
            if num in map:
                return True
            map.add(num)
        return False