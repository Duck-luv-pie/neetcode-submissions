class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x:x[1])

        cur_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < cur_end:
                count += 1
            else:
                cur_end = end
        return count