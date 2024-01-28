class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i,n in enumerate(nums):
            twoSum = target - n
            if twoSum in lookup:
                return [lookup[twoSum], i]
            else:
                lookup[n] = i
        
                