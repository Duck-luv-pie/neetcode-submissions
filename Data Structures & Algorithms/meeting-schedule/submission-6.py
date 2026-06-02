"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)

        cur_start = intervals[0].start
        cur_end = intervals[0].end

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end

            if start < cur_end:
                return False
            else:
                cur_start = start
                cur_end = end
        return True