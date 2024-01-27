class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        helper = dict()
        for i in range(97, 123):
            helper[i] = 0
        
        temp1 = helper.copy()
        
        for i in range(len(s1)):
            temp1[ord(s1[i])]+=1
        
        temp2 = helper.copy()
        
        for j in range(len(s1)-1):
            temp2[ord(s2[j])]+=1
            
        l,r = 0, len(s1)-1
        while r < len(s2):
            temp2[ord(s2[r])]+=1
            if temp1 == temp2:
                return True
            temp2[ord(s2[l])]-=1
            l+=1
            r+=1
        return False
        