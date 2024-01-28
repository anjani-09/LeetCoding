class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'}':'{',']':'[',')':'('}
        stack = []
        for i in s:
            if i in lookup.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if not lookup[i] == stack[-1]:
                        return False
                    else:
                        stack.pop()
        if not stack:
            return True
        return False
        
        