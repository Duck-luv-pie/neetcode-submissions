class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            ')': '(', '}': '{', ']': '['
        }
        for char in s:
            if char in hmap:
                if stack and stack[-1] == hmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack