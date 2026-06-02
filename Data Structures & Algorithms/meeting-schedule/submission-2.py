"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        res = []
        if not intervals:
            return True
        cur_start, cur_end = intervals[0].start, intervals[0].end

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end
            if start < cur_end:
                return False
            else:
                cur_start = start
                cur_end = end
        return True