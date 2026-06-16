class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def condition(middle):
            total_h = 0;
            for pile in piles:
                total_h += -(pile//-middle)
            return total_h <= h
            
                


        while l < r:
            mid = (l+r)//2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l
            