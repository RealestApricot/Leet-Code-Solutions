class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        right = (len(needle))
        for i in range(len(haystack)):
            if haystack[i:right] == needle:
                return i
            right += 1
            if right > len(haystack): break
        return -1