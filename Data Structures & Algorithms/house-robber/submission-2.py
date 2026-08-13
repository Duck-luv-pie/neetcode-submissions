class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            max_profit = nums[0]
            return nums[0]
        
        if len(nums) == 2:
            max_profit = max(nums[0], nums[1])
            return max_profit

        
        array = [0] * len(nums)

        array[0] = nums[0]
        array[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            skip_profit = array[i - 1]
            rob_profit = array[i-2] + nums[i]

            max_profit = max(skip_profit, rob_profit)

            array[i] = max_profit
        
        return array[-1]