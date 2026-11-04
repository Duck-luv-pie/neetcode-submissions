class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for first_index in range(len(nums) - 2):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue
            
            left = first_index + 1
            right = len(nums) - 1

            while left < right:
                cur_sum = nums[first_index] + nums[left] + nums[right]
                if cur_sum == 0:
                    res.append([nums[first_index], nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
            
                


        return res
                