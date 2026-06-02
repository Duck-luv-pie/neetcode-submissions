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
        start_cur = intervals[0].start
        end_cur = intervals[0].end
        for interval in intervals[1:]:
            start = interval.start
            end = interval.end
            if start < end_cur:
                return False
            else:
                start_cur = start
                end_cur = end
        return True
            
