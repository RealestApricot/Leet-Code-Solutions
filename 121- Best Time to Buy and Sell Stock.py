class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        BuyIndex = 0
        SellIndex = 1
        while SellIndex < len(prices):
            if prices[BuyIndex] < prices[SellIndex]:
                if prices[SellIndex] - prices[BuyIndex] > MaxProfit:
                    MaxProfit = prices[SellIndex] - prices[BuyIndex]
            else:
                BuyIndex = SellIndex
            SellIndex += 1
        return MaxProfit
