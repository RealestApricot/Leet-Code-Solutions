class Solution:
    def isPalindrome(self, s: str) -> bool:
        Alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        Temp = ""
        for i in range(len(s)):
            if s[i:i+1].lower() in Alphabet:
                Temp += s[i:i+1].lower()

        Temp.replace(" ", "")
        s = Temp
        if len(s) == 1:
            return True
        for i in range(len(s)//2):
            Substring1 = s[i]
            Substring2 = s[-i-1]
            if Substring1 != Substring2:
                return False
        return True
