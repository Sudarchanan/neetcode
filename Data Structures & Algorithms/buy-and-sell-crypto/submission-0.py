class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        len_price = len(prices)
        for i in range(len_price):
            for j in range(i + 1, len_price):
                minProfit = max(0, prices[j] - prices[i])
                maxProfit = max(maxProfit, minProfit)
        return maxProfit