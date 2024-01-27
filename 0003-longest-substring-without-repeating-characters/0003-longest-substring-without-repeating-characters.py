class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        longest = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in charSet:
                charSet.add(s[i])
            else:
                while s[i] in charSet:
                    charSet.remove(s[l])
                    l+=1
                charSet.add(s[i])
            longest = max(longest, len(charSet))
        return longest
        
                