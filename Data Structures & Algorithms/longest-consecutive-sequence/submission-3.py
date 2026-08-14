class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maximum = 0

        for num in nums:
            if num -1 not in nums: #this means we have a new chain
                cur_num = num
                cur_length = 1

                while cur_num + 1 in nums:
                    cur_num += 1
                    cur_length += 1
                maximum = max(cur_length, maximum)
        
        return maximum
            