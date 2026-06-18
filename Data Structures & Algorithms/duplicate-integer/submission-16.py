class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {} #we will add all seen numbers into dict to compare

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        return False 