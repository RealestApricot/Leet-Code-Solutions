class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) < 2:
            return 0
        for index in range(len(prices)-1):
            if prices[index] < prices[index + 1]:
                maxProfit += prices[index + 1] - prices[index]
        return maxProfit