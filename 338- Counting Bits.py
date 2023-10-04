class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = str(bin(i)).count("1")
        return ans
