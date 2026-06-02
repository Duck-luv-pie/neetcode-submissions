class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

        return False
        
        # og_length = len(nums)
        # nums = set(nums)
        # if len(nums) < og_length:
        #     return True
        # return False

            