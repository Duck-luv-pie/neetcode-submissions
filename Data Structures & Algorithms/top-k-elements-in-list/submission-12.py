from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we need to count the frequency of each number
            #dictionary key: num, value: freq
        
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        #we need to sort by frequency
            #buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)


        #return the first k values
            #add to a result and if length is k then return
        res = []
        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return -1







