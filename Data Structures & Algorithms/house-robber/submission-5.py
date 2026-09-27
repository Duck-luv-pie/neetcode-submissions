class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        n = len(nums)

        def dfs(i):
            if i >= n: #if it's invalid return 0 (cause we can't add)
                return 0
            
            if i in memo: #we have seen the answer so return it
                return memo[i]

            rob_current = nums[i] + dfs(i + 2)
            skip_current = dfs(i + 1)
            memo[i] = max(rob_current, skip_current)
            return memo[i]
        
        return dfs(0)
