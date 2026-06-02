from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a dictionary of elements and their frequencies
        count = Counter(nums)

        #create freq buckets and add elements
        buckets = [[] for _ in range(len(nums) + 1)] #+1 for the 0th bucket

        for num, freq in count.items():
            buckets[freq].append(num)

        #iterates backwards most freq to least until k elements are appended to res
        res = []

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
