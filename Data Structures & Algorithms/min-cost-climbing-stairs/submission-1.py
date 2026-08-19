class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #given that we can either go up 1 or 2 floors:
        #dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        #meaning we need two smallest ones
        dp = [float('inf')] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    
        return dp[len(cost)]
