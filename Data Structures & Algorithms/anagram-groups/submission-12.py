class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} #key will be the tuple of alphas, value will be a list of list of str

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            key = tuple(alpha)

            if key in res:
                res[key].append(string)
            else:
                res[key] = [string]
        
        return list(res.values())