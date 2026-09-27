class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_char = {}

        for char in s:
            map_char[char] = map_char.get(char, 0) + 1
        
        for char in t:
            map_char[char] = map_char.get(char, 0) - 1
            if map_char[char] == 0:
                del map_char[char]
        
        return map_char == {}
        
