class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        og = len(nums)
        nums = set(nums)
        new = len(nums)

        if new < og:
            return True
        else:
            return False