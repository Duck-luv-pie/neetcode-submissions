class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []

        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:

            if start <= cur_end:
                cur_end = max(cur_end, end)
            else:
                res.append([cur_start, cur_end])
                cur_start = start
                cur_end = end
        res.append([cur_start, cur_end])
    
        return res

            