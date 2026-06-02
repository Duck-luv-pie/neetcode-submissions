class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #get the length of the output
        n = len(nums)

        res = [1] * n

        #calculate the prefix
        prefix = 1
        #iterate through the nums and put prefix value in res and then update prefix for next prefix
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        #calculate the postfix 
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        #return the result
        return res

