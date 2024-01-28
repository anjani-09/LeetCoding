class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        
        for n in nums:
            if n in lookup:
                return True
            lookup[n] = 1 
        return False
        