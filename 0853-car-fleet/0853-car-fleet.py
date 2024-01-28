class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        helper = []
        for p,s in zip(position, speed):
            helper.append([p,s])
        helper.sort(reverse = True)
        stack = []
        for p,s in helper:
            time = (target - p)/s
            stack.append(time)
            if len(stack) > 1 and (stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)
            
            
            
            
        