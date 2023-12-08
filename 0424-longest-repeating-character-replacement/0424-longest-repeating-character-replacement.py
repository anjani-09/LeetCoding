class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        maxf = 0
        l = 0
        res = 0
        for r in range(len(s)):
            lookup[s[r]] = 1 + lookup.get(s[r],0)
            maxf = max(lookup.values())
            if (r - l + 1) - maxf > k:
                lookup[s[l]] -= 1
                l+=1
            else:
                res = max(res, r - l + 1)
        return res
        