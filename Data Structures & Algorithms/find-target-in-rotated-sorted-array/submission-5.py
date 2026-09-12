class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        def condition(mid):
            if nums[mid] > nums[r]:
                return False
            return True

        while l < r:
            mid = (l + r) //2

            if condition(mid):
                r = mid
            else:
                l = mid + 1
            
            #now we have where the minimum lives at l 
        offset = l

        #so 4 -> 0, 4 - 1 -> len(nums) - 1

        l, r = 0, len(nums) - 1 

        while l <= r:
            mid = (l +r)//2
            if nums[(mid+offset) % len(nums)] == target:
                return (mid+offset) % len(nums)
            elif nums[(mid+offset) % len(nums)] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1 