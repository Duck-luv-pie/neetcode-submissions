class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(start, remaining):      
            if remaining == 0:
                res.append(path[:])
                return
            for j in range(start, len(nums)):
                c = nums[j]

                if c > remaining:
                    break
                
                path.append(c)
                dfs(j, remaining - c)
                path.pop()
        
        dfs(0, target)

        return res