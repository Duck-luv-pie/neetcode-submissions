class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}

        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        #we need to check for each part if there exists that permutation


        #now we go through s2 in a fixed sliding window of length s1 and see if it matches

        l = 0
        s2_map = {}

        if len(s2) < len(s1):
            return False

        for i in range(len(s2)):
            s2_map[s2[i]] = s2_map.get(s2[i], 0 ) + 1
        
            while  sum(s2_map.values()) > len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    s2_map.pop(s2[l], None)
                l += 1
            
            if s1_map == s2_map:
                return True
        
        return False
