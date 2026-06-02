from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}

        for char in s1:
            if char in dict_s1:
                dict_s1[char] += 1
            else:
                dict_s1[char] = 1
            
        l = 0
        dict_s2 = {}
        for r in range(len(s2)):
            if s2[r] in dict_s2:
                dict_s2[s2[r]] += 1
            else:
                dict_s2[s2[r]] = 1
            while (r - l + 1) > len(s1):
                if dict_s2[s2[l]] > 1:
                    dict_s2[s2[l]] -= 1
                else:
                    del dict_s2[s2[l]]
                l += 1
            if dict_s1 == dict_s2:
                return True
        return False
        
            



        
            
