class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        l = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l += 1
            seen[s[right]] = 1

            max_length = max(max_length, right - l + 1)

        return max_length

            