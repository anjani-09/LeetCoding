class Solution:
    def isValid(self, s: str) -> bool:
        lookup = { '}':'{', ']':'[', ')':'(' }
        stack = []
        for char in s:
            if char in lookup.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1]!= lookup[char]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True

        