class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        freq_bucket = [[] for _ in range(len(nums) + 1)] #where the first is for freq 0

        for num, freq in count.items():
            freq_bucket[freq].append(num)

        res = []
        
        for i in range(len(freq_bucket) -1, 0, -1):
            for num in freq_bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
