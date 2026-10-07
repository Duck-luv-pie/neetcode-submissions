class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the offset then search in array with that offset

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        #now we have l at the offset, remember this is the index of it and we can do reg bs with an offset
        offset = l
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            real = (mid + offset) % len(nums)
            if nums[real] == target:
                return real
            elif nums[real] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

                











