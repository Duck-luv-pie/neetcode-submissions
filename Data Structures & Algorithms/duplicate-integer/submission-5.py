class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(set(nums))
        if n != len(nums):
            return True
        return False
