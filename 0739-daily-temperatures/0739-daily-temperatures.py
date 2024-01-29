class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*(len(temperatures))
        stack = []
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackI, stackT = stack.pop()
                res[stackI] = ind - stackI
            stack.append([ind, temp])
        return res
                
        