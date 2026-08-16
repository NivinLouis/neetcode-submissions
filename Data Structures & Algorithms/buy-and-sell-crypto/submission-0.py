class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxprofit = 0

        while r<len(prices):
            profit = prices[r]-prices[l]
            maxprofit = max(maxprofit,profit)
            
            if prices[r]<prices[l]:
                l=r
            
            r=r+1

        return maxprofit