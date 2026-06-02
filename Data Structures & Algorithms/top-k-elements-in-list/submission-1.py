class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # 2. Bucket sort: index = frequency
        # Max possible frequency is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for n, count in freq.items():
            buckets[count].append(n)
        
        # 3. Collect from highest frequency down
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result
        

        