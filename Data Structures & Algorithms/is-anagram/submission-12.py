from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hmap = Counter(s)
        #for s go through and count


        t_hmap = Counter(t)
        #for t go through and count

    
        #compare hashmaps
        if s_hmap == t_hmap:
            return True
        return False