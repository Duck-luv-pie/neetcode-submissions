class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            dif = target - numbers[i]
            if dif in seen:
                return [seen[dif]+1, i+1]
            seen[numbers[i]] = i 