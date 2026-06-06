class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            key = tuple(alpha)
            if key in hmap:
                hmap[key].append(string)
            else:
                hmap[key] = [string]
        return list(hmap.values())