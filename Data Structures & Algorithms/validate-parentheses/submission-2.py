class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)
        dictionary = {'}': '{', ']': '[', ')': '('}
        for char in s:
            if char in dictionary.values(): #checking if it is an open bracket
                stack.append(char)
            elif char in dictionary: #checking if it is a closed bracket
                if not stack or stack[-1] != dictionary[char]:
                    return False
                stack.pop()
        return not stack
        