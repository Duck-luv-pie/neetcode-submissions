class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count how many of each element there is
        #return the k most frequent elements in a list of ints

        #first count frequency of elements
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        #find out which elements are the k most frequent - buckets approach

        buckets = [[] for _ in range(len(nums) + 1)] #accounts for the 0 freq

        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []

        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return -1
