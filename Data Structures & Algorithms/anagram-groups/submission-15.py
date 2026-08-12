class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            
            key = tuple(alpha)
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]
        
        return list(groups.values())