class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minimum_price = prices[0]
        maximum_profit = 0

        for price in prices:
            minimum_price = min(minimum_price, price)
            cur_profit = price - minimum_price

            maximum_profit = max(maximum_profit, cur_profit)
        
        return maximum_profit