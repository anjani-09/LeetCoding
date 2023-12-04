class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            d = {}
            for i,n in enumerate(nums):
                twoSum = target - n
                if twoSum in d:
                    return [d[twoSum],i]
                d[n] = i
                
                
        