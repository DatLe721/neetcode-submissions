class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = [] 
        for i in range(len(prices)):
            if i == 0 :
                maxP.append(prices[len(prices)-1])
            else: 
                maxP.append(max(maxP[i-1],prices[len(prices)-1-i]))
        highest = 0
        print(maxP)
        for i in range(len(prices)):
            highest = max(highest,(maxP[len(prices)-1-i]-prices[i]))
        return highest