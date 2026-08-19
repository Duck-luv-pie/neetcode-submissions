class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] = either we can steal from this one or not.
        #if we steal from this one, we can't steal from the one before us
        #if we don't steal from this one, it we stole from the one before us

        #dp[i] = max(dp[i-2] + nums[i], dp[i-1]) so it means we need two base cases
        #dp[i] represents the amount of money we have stolen so far

        dp = [float('inf')] * (len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        
        return dp[len(nums)]
