class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(mid):
            total_hour = 0
            for pile in piles:
                total_hour += (pile + mid - 1)// mid
            return total_hour <= h
        l,r = 1, max(piles)

        while l < r:
            mid = (l+r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l