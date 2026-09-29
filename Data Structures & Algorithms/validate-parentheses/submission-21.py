class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ']': '[', ')': '('}

        stack = []


        for char in s:
            if char in pairs: #meaning that it is an ending bracket
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            
            else:
                stack.append(char)
        
        return True if stack == [] else False