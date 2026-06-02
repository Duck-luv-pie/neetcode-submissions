class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if t == "+":
                    operation = a + b
                elif t == "-":
                    operation = a - b
                elif t == '*':
                    operation = a * b
                else:
                    operation = a / b
                stack.append(int(operation))
        return stack[-1]
            
                
                