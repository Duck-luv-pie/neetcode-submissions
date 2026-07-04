class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1

        cur_area = 0
        max_area = 0
        cur_height = 0

        while l < r:
            cur_height = min(heights[l], heights[r])
            cur_area = cur_height * (r-l)
            max_area = max(max_area, cur_area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_area