class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = res = 0
        
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxf = max(counter.values())
            if r - l + 1 - maxf <= k:
                res = max(res, r - l + 1)
            else:
                counter[s[l]]-=1
                l+=1
        return res
        