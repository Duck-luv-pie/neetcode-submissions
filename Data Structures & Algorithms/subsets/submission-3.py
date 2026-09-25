class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            #if we reached the subset
            if i == len(nums):
                res.append(path[:])
                return

            #we can skip subsets
            path.append(nums[i])
            backtrack(i + 1)

            path.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res