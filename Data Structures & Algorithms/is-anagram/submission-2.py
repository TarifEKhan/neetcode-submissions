class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        map_2 = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 0
        
        for char in t:
            if char in map_2:
                map_2[char] += 1
            else:
                map_2[char] = 0
        return map == map_2