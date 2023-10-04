class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)-1):
            if len(s) % (i+1) != 0:
                continue
            if "".join([s[0:i+1]]*(len(s)/(i+1))) == s:
                return True
        return False
