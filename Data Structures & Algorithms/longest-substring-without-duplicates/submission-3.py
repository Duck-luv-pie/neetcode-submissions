class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hmap = {}
        max_length = 0

        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            while hmap[s[r]] != 1:
                if s[l] in hmap:
                    if hmap[s[l]] > 1:
                        hmap[s[l]] -= 1
                    else:
                        del hmap[s[l]]
                    l += 1
            max_length = max(max_length, r - l + 1)
        
        return max_length
