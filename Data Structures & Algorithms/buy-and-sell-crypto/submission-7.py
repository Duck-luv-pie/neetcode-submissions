class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            lowest_price = min(price, lowest_price)
            cur_profit = price  - lowest_price
            max_profit = max(max_profit, cur_profit)
        
        return max_profit