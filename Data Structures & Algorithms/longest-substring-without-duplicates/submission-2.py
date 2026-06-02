class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        l = 0
        maximum = 0

        for r in range(len(s)):
            unique[s[r]] = unique.get(s[r], 0) + 1

            while unique.get(s[r], 0) > 1:
                unique[s[l]] -= 1
                l += 1
            maximum = max(maximum, r-l+1)
        return maximum


