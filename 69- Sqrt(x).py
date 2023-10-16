class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        closestInt = 1
        for i in range(x):
            if i*i > x:
                break
            if i * i <= x < (i + 1) * (i + 1):
                closestInt = i
        return closestInt
