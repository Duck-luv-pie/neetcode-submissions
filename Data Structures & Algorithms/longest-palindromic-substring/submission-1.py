class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_length, len_length = 0, 0

        def expand(l, r):
            nonlocal l_length
            nonlocal len_length

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            #but now we expanded past by 1 too much on both sides
        
            length = r - l - 1
            if len_length < length:
                l_length, len_length = l + 1, length 
            
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[l_length:l_length + len_length]