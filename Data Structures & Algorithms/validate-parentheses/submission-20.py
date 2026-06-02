class Solution:
    def isValid(self, s: str) -> bool:
        #dictionary key: closing, value: opening to compare
        pairs = {']': '[', '}': '{', ')': '('}

        #stack to compare order
        stack = []

        #if we have a open bracket add to stack, if we have closed check top
        for char in s:
            if char in '[]{}()':
                if char in pairs: #this is a closing bracket
                    #check top of stack to see if matching
                    if stack and stack[-1] == pairs[char]:
                        stack.pop()
                    else:
                        return False
                    
                else: #these are opening brackets
                    stack.append(char)
        return not stack



