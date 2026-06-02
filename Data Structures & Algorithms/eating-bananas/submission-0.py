class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(mid):
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            return hours <= h

        l, hi = 1, max(piles)

        while l < hi:
            mid = (l + hi) // 2
            if condition(mid):
                hi = mid
            else:
                l = mid + 1
        return l
