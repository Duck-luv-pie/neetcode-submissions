class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = set(nums)
        if n != len(nums):
            return True
        return False