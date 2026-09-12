class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l = 0

        for right in range(len(prices)):
            cur_profit = prices[right] - prices[l]
            max_profit = max(max_profit, cur_profit)

            if prices[right] < prices[l]:
                l = right
        
        return max_profit