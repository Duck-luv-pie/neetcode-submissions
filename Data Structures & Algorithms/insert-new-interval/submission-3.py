class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        flag = False
        #basically go through intervals and see if it slides neatly before newinterval, if yes add it
        for start, end in intervals:
            if end < newInterval[0]:
                res.append([start, end]) #if it is before the interval, add start/end
            
            #if it does not slide neatly through, we gotta merge
            
            elif start > newInterval[1]:
                if not flag:
                    res.append(newInterval)
                res.append([start, end])
                flag = True
            elif end >= newInterval[0]: 
                newInterval[0] = min(newInterval[0], start) #we gotta find the min for the start and max for the end
                newInterval[1] = max(newInterval[1], end)
            
        if not flag:
            res.append(newInterval)
        
        return res
