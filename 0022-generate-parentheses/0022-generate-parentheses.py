class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(fOpen, fClose,stack):
            if fOpen == fClose == n:
                res.append(''.join(stack))
                return
            if fOpen < n:
                stack.append('(')
                backtrack(fOpen+1, fClose, stack)
                stack.pop()
            if fClose < fOpen:
                stack.append(')')
                backtrack(fOpen, fClose+1, stack)
                stack.pop()
        backtrack(0,0, [])
        return res
        