class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            key = tuple(alpha)

            if key in sublists:
                sublists[key].append(string)
            else:
                sublists[key] = [string]
            
        return list(sublists.values())