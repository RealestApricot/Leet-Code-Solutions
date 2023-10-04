class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Longest = 0
        Substring = ""
        for Index in range(len(s)):
            if s[Index] in Substring:
                while s[Index] in Substring:
                    Substring = Substring[1:]
                Substring += s[Index]
            else:
                Substring += s[Index]
                Longest = max(Longest, len(Substring))
        return Longest