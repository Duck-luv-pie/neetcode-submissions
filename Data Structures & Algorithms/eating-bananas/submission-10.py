class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def condition(mid):
            count_h = 0
            for pile in piles:
                count_h += math.ceil(pile/mid)
            return count_h <= h
        
        while l < r:
            mid = (l+r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        
        return l