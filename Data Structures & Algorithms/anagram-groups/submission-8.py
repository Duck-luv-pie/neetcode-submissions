class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each string find which anagram group it belongs to 

        hmap = {}

        #for each string find the number of each char
        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            key = tuple(alpha)
            #check this key against our current database
            if key in hmap:
                hmap[key].append(string) #add to the database
            else:
                hmap[key] = [string] #add to the database
            
        return list(hmap.values())
            


        

        
