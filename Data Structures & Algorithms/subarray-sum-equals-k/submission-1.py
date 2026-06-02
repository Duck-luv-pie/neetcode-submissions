from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        cur_sum = 0
        res = 0

        for num in nums:
            cur_sum += num

            res += count[cur_sum - k]

            count[cur_sum] += 1

        return res