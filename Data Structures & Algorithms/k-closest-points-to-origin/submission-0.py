import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            heapq.heappush(heap, [distance, x, y])

        while len(res) != k:
            arr = heapq.heappop(heap)
            res.append([arr[1], arr[2]])

        return res