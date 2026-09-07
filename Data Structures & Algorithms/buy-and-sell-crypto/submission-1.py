class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        highest = 0
        lowest = prices[0] 
        for price in prices:
            if price< lowest:
                lowest = price
            if highest < (price-lowest):
                highest = price-lowest
        return highest
