class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen: #get rid of stuff on the left side
                seen.remove(s[l])
                l += 1
            #now everything is unique
            seen.add(s[right])
            max_length = max(max_length, len(seen))

        
        return max_length







