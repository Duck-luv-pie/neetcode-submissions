class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(k):
            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + k - 1) // k
            return hours_spent <= h
        l,r = 1, max(piles)
        
        while l < r:
            m = (l+r) // 2
            if condition(m):
                r = m
            else:
                l = m + 1
        return l