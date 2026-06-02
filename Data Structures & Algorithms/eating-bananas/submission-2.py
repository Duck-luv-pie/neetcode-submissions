class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(mid):
            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + mid -1)//mid
            return hours_spent <= h
        l,r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l