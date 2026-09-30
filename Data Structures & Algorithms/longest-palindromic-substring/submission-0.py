class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_length, res_length = 0, 0

        def expand(l, r):
            nonlocal l_length
            nonlocal res_length

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            #this causes an overshoot:
            length = r - l - 1

            if length > res_length:
                l_length, res_length = l + 1, length
            
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[l_length:l_length + res_length]