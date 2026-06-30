class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        ans = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                ans = max(ans, prices[sell]-prices[buy])
            else:
                buy = sell

            sell += 1
        return ans

