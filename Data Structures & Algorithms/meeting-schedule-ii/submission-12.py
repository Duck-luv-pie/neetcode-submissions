import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        min_rooms = 0

        intervals.sort(key=lambda x:x.start)

        for interval in intervals:
            start = interval.start
            end = interval.end

            if heap and start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
            min_rooms = max(min_rooms, len(heap))
        return min_rooms


