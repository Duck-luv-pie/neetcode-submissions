class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer from both ends
        l,r = 0, len(numbers) - 1

        while l < r:
            cur_sum = (numbers[l]+numbers[r])
        
            if target == cur_sum:
                return [l+1, r+1]
        #if target is smaller move left pointer
            elif target < cur_sum:
                r -= 1

        #if target is bigger move right pointer
            else: 
                l += 1
        return -1