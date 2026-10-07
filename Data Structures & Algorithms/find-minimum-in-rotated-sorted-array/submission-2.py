class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        def condition(mid, r):
            #is mid smaller than right?
            return nums[mid] < nums[r]

        while l < r:
            mid = (l + r) // 2

            if condition(mid, r):
                r = mid
            else:
                l = mid + 1
        
        return nums[l]