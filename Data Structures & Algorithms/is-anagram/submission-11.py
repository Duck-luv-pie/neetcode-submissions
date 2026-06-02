class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two ways to do this one
        #case 1: go through each char and count num to use as key O(n)
        #case 2: sort each to make a key O(nlogn) <--

        #loop through char in s
            #count char and add to dictionary
        
        seen_s = {}
        seen_t = {}

        for char in s:
            if char in seen_s:
                seen_s[char] += 1
            else:
                seen_s[char] = 1

        #loop through char in t
            #count char and add to dictionary

        for char in t:
            if char in seen_t:
                seen_t[char] += 1
            else:
                seen_t[char] = 1
        
        return (seen_s == seen_t)

        



