class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        helper = [[p,s] for p,s in zip(position, speed)]
        helper.sort(reverse = True)
        
        stack = []
        
        for p,s in helper:
            stack.append((target - p)/s)
            
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack)
        