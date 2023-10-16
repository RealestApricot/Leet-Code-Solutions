class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        substr = ""
        for i in range(len(s)):
            if s[len(s)-i-1] == " ":
                if len(substr) > 0:
                    return len(substr)
            else:
                substr += (s[len(s)-i-1])
        return len(substr)
