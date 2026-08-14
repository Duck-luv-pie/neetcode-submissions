class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}


        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
            if hmap[num] == len(nums)//2 + 1:
                    return num
        
