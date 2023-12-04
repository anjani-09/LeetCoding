class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        for c in s:
            s_d[c] = 1 + s_d.get(c,0)
        for c in t:
            t_d[c] = 1 + t_d.get(c,0)
        return s_d == t_d
        