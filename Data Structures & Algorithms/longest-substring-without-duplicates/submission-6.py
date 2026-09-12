class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_length = 0

        for char in s:
            if char in seen:
                while s[l] != char:
                    seen.remove(s[l])
                    l += 1
                #now s[l] is at that char
                l += 1

            else:
                seen.add(char)
            
            max_length = max(max_length, len(seen))
        
        return max_length