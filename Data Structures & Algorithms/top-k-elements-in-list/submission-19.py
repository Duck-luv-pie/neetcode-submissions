from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        
        buckets = [[] for _ in range(len(nums) + 1)]
        

        for num, freq in count.items():
            buckets[freq].append(num)
        
        for freq in range(len(nums), -1, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        
