class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res, path = [], []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for j in range(start, len(nums)):
                c = nums[j]

                if c > remaining:
                    break
                
                path.append(c)
                backtrack(j, remaining - c)
                path.pop()
        
        backtrack(0, target)
        return res