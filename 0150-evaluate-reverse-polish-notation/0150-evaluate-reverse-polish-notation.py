class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        
        for token in tokens:
            if token not in operators:
                stack.append(token)
                continue
            b,a = int(stack.pop()), int(stack.pop())
            if token == "+":
                stack.append(str(a + b))
            elif token == "-":
                stack.append(str(a - b))
            elif token == "/":
                stack.append(str(int(a/b)))
            else:
                stack.append(str(a*b))
        return int(stack[0])
                
    
        