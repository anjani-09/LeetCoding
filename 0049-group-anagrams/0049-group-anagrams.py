class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)-1,-1,-1):
            word = strs[i]
            key = ''.join(sorted(word))
            res[key].append(word)
        return res.values()
        