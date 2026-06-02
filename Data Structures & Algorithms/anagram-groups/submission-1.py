class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            alpha = tuple(alpha)
            if alpha in res:
                res[alpha].append(string)
            else:
                res[alpha] = [string]
        return list(res.values())
