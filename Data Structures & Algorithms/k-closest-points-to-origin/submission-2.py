import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = (math.sqrt((x - 0)**2 + (y - 0)**2))
            heapq.heappush(heap, (distance, x, y))
        
        res = []

        while len(res) < k:
            distance, x, y = heapq.heappop(heap)

            res.append([x,y])
        
        return res