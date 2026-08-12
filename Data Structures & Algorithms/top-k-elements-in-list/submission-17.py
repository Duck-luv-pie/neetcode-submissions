from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:\

        res = []
        #put into dictionary of count
        count = Counter(nums)

        #make buckets key = num, val = count
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num) 

        #iterate thoruhg buckets backwards until res = k length
        for i in range(len(nums), 0, -1):
            while buckets[i]:
                res.append(buckets[i][-1])
                buckets[i].pop()
                if len(res) == k:
                    return res
            
