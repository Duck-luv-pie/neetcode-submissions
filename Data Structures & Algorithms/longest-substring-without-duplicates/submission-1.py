class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            else: #not in seen
                seen.add(s[r])
                r += 1
                length = max(length, r-l)
        return length


        
        