class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {']': '[', '}': '{', ')': '('}

        for char in s:
            if char in hmap:
                if stack:
                    if stack[-1] != hmap[char]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            if char not in hmap: #prob opening bracket
                stack.append(char)
        return not stack