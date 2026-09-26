class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res, path = [], []

        def dfs(start, remaining):
            if remaining == 0:
                    res.append(path[:])
                    return

            for j in range(start, len(candidates)):

                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                
                #now get rid of c
                c = candidates[j]

                if c > remaining:
                    break

                path.append(c)
                dfs(j + 1, remaining - c)
                path.pop()
            
        dfs(0, target)
        return res

            