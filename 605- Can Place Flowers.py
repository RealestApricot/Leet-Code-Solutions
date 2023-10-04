class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowerSpots = 0
        for i in range(len(flowerbed)):
            backClear = False
            frontClear = False
            if (i > 0 and flowerbed[i-1] != 1) or (i == 0):
                backClear = True
            if (i < len(flowerbed)-1 and flowerbed[i+1] != 1) or (i == len(flowerbed)-1):
                frontClear = True
            if backClear == True and frontClear == True and flowerbed[i] != 1:
                flowerSpots += 1
                flowerbed[i] = 1
        return flowerSpots >= n
