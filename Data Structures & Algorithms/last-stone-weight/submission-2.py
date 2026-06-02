import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) #max heap
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(x-y))
        return (-stones[0] if stones else 0)
