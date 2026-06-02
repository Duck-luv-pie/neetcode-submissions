from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        hp = []

        for num, freq in count.items():
            heapq.heappush(hp, (freq, num))
        while len(hp) > k:
            heapq.heappop(hp)
        return [num for (freq, num) in hp]