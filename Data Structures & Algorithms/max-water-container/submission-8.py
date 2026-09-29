class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur_area = 0
        max_area = 0

        l,r = 0, len(heights) -1 
        l_max = heights[0]
        r_max = heights[-1]


        while l < r:
            l_max = max(l_max, heights[l])
            r_max = max(r_max, heights[r])

            cur_area = (r - l) * min(l_max, r_max)
            max_area = max(max_area, cur_area)

            if l_max <= r_max:
                l += 1
            else:
                r -= 1
        
        return max_area


