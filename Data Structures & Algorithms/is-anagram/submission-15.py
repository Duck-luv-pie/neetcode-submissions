class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #for each char in s: count the # of char
        hmap_s = {}
        for char in s:
            if char in hmap_s:
                hmap_s[char] += 1
            else:
                hmap_s[char] = 1

        #for each char in t: count the # of char
        hmap_t = {}
        for char in t:
            if char in hmap_t:
                hmap_t[char] += 1
            else:
                hmap_t[char] = 1

        #compare the results
        return (hmap_s == hmap_t)