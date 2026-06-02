class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        buckets = [[] for __ in range(len(nums)+1)]

        for num, freq in hashmap.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result
        