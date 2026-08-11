class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bruteforce
        maxProfit = 0
        len_price = len(prices)
        for i in range(len_price):
            for j in range(i + 1, len_price):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return maxProfit