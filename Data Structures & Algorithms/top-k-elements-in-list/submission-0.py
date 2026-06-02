class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        count = [[] for _ in range(len(nums)+ 1)]

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        for num, f in dictionary.items():
            count[f].append(num)
        
        returns = []
        for i in range(len(nums), 0, -1):
            for x in count[i]:
                returns.append(x)
            if len(returns) == k:
                return returns