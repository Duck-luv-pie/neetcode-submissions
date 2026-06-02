class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[(ord(char) - ord('a'))] += 1
            if tuple(alpha) in res:
                res[tuple(alpha)].append(string)
            else:
                res[tuple(alpha)] = [string]
        
        return list(res.values())

                
