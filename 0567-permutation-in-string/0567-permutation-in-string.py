class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       
        if len(s1) > len(s2):
            return False
        helper = {}
        
        for i in range(97, 123):
            helper[i] = 0
        helper1 = helper.copy()
        helper2 = helper.copy()
        
        for i in range(len(s1)):
            helper1[ord(s1[i])]+=1
        for i in range(len(s1)-1):
            helper2[ord(s2[i])]+=1
        
        l,r = 0, len(s1)-1
        while r < len(s2):
            helper2[ord(s2[r])] += 1
            if helper1 == helper2:
                return True
            helper2[ord(s2[l])]-=1
            l+=1
            r+=1
        return False
        
        