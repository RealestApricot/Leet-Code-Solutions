class Solution:
    def reverse(self, x: int) -> int:
        Negative = False
        if x < 0:
            Negative = True
            x *= -1
        ReturnNum = 0
        while x > 0:
            ReturnNum += x % 10
            x = x//10
            if x > 0:
                ReturnNum *= 10
            if ReturnNum > (2**31)-1 or ReturnNum < (-2**31):
                ReturnNum = 0
                break
        if Negative == True:
            ReturnNum *= -1
        return ReturnNum
