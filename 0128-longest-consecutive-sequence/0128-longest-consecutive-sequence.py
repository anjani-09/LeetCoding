class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #identify the sequence starting element and then continue to find the longest sequence
        
        #remove duplicates
        
        numSet = set(nums)
        result = 0
        for n in numSet:
            longest = 0
            if n-1 in numSet:
                continue
            while n+longest in numSet:
                longest+=1
            result = max(result, longest)
        return result
                
                
            
        