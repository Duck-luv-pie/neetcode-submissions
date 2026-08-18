class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        #go through all intervals and see if we can merge them?
        #we can merge if the ending of i is smaller or equal to start of i + 1
        start, end = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            if end >= interval[0]: #ending of i-1 is smaller than start of i   
                start = min(interval[0], start)
                end = max(interval[1], end)
            else:
                res.append([start, end]) #there is no overlap
                start, end = interval[0], interval[1]
            #what if we merged the last one though? then we wouldn't 
        
        res.append([start, end])

        return res
