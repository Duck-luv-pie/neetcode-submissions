class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for r in range(0, len(numbers)):
            missing = target - numbers[r]
            if missing in seen:
                return [seen[missing] + 1, r+ 1]
            else:
                seen[numbers[r]] = r
        return -1
