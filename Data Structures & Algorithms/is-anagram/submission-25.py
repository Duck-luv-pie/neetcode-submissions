class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}

        for char in s:
            dictionary[char] = dictionary.get(char, 0) + 1
        
        for char in t:
            dictionary[char] = dictionary.get(char, 0) - 1
            if dictionary[char] == 0:
                del dictionary[char]
        
        return dictionary == {}