class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r,l = 0,0
        n = len(prices)
        maxprice = 0
        while r < n:
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxprice = max(maxprice, profit)
            r += 1
        return maxprice