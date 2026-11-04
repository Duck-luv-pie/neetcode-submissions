class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []


        for first_index in range(len(nums) - 2):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue
            
            l = first_index + 1
            r = len(nums) - 1

            while l < r:
                cur_sum = nums[first_index] + nums[l] + nums[r]

                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    #now cur_sum == 0
                    res.append([nums[first_index], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
        return res