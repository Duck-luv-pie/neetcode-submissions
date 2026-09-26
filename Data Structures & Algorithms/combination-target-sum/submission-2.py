class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()


        res, path = [], []

        def backtrack(start, remaining):
            for j in range(start, len(nums)):
                c = nums[j]
            #we want to check if we have the combined sum
                if remaining == 0:
                    res.append(path[:])
                    return
                
                #now we know that we have not reach it
                #case 1: we will overshoot

                if c > remaining:
                    break
                
                #case #2 we undershoot
                path.append(nums[j])
                backtrack(j, remaining - c)
                path.pop()
            
        backtrack(0, target)
        return res


