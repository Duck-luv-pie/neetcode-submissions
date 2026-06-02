class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            want = target - num
            if want in seen:
                return [seen[want], i]
            else:
                seen[num] = i
        return []