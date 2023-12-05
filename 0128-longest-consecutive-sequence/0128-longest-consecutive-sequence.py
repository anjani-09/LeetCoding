class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #remove the duplicates
        nums = set(nums)
        #check if the current element is starting element of a sequence and try to find longest sequence
        res = 0
        for n in nums:
            longest = 0
            if n - 1 not in nums:
                while n + longest in nums:
                    longest+=1
                res = max(res, longest)
        return res
                
        