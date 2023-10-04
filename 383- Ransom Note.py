class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        CharCount = {}
        for char in magazine:
            CharCount[char] = CharCount.get(char, 0) + 1
        for char in ransomNote:
            CharCount[char] = CharCount.get(char, 0) - 1
            if CharCount[char] < 0:
                return False
        return True
