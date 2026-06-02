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
        if not intervals:
            return True
        cur_start = intervals[0].start
        cur_end = intervals[0].end

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end

            if cur_end > start:
                return False
            else:
                cur_start = start
                cur_end = end

        return True
