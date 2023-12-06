class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for char in s:
            while char in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(char)
            res = max(res, len(charSet))
        return res
            