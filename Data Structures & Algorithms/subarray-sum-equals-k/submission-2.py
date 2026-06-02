from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        cur_sum = 0
        res = 0

        for num in nums:
            cur_sum += num
            res += count.get(cur_sum-k, 0)
            count[cur_sum] = count.get(cur_sum, 0) + 1
        return res