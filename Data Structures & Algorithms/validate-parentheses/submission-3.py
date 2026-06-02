class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')': '(', '}': '{', ']': '['}
        for char in list(s):
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary:
                if not stack or stack[-1] != dictionary[char]:
                    return False
                stack.pop()
        return not stack
        