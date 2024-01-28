class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        
        for i,n in enumerate(numbers):
            twoSum = target - n
            if twoSum in lookup:
                return [lookup[twoSum]+1, i+1]
            lookup[n] = i
        
        