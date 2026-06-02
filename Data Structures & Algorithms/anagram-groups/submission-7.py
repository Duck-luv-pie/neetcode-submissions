class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            alpha = tuple(alpha)
            if alpha in hmap:
                hmap[alpha].append(string)
            else:
                hmap[alpha] = [string]

        return list(hmap.values())