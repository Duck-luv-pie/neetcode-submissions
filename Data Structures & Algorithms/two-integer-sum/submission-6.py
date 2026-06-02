class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in hash:
                return [hash[missing], i]
            else:
                hash[nums[i]] = i