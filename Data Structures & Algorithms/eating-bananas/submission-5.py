class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def condition(mid):
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours <= h:
                return True
            else:
                return False

        l,r = 1, max(piles)

        while l < r:
            mid = (l+r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l
