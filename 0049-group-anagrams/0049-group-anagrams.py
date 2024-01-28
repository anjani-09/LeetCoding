class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = defaultdict(list)
        
        for word in strs[::-1]:
            output[''.join(sorted(word))].append(word)
        
        return output.values()