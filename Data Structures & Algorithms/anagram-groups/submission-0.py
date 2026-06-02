class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sort = tuple(sorted(string))
            if sort in hashmap:
                hashmap[sort].append(string)
            else:
                hashmap[sort] = [string]
        
        return list(hashmap.values())

        

        
        