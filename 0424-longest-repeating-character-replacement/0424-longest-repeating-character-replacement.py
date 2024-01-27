class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        max_f = 0
        l = 0
        res = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r],0)
            max_f = max(counter.values())
            if (r - l + 1) - max_f <= k:
                res = max(res, r - l + 1)
            else:
                if counter[s[l]] == 1:
                    del counter[s[l]]
                else:
                    counter[s[l]]-=1
                l+=1
        return res
                