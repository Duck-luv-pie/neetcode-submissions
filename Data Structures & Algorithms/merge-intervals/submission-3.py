class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        if not intervals:
            return [1]
        prev_start, prev_end = intervals[0]
        res = []

        for new_start, new_end in intervals[1:]:
            #we gotta check if it overlaps at all
            if prev_end < new_start:
                res.append([prev_start, prev_end])
                prev_start = new_start
                prev_end = new_end
            else:
            # now we know if will merge 
                prev_start = min(prev_start, new_start)
                prev_end = max(prev_end, new_end)
        
        res.append([prev_start, prev_end])
        
        return res