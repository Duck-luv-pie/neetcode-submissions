class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j-1]:
                    continue
                
                c = candidates[j]

                if c > remaining:
                    break
                
                path.append(c)
                backtrack(j + 1, remaining - c)
                path.pop()
        
        backtrack(0, target)
        return res