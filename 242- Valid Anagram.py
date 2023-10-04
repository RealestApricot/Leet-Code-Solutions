class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        SValues = {}
        TValues = {}
        for char in s:
            SValues[char] = SValues.get(char, 0) + 1
        for char in t:
            TValues[char] = TValues.get(char, 0) + 1

        return SValues == TValues
