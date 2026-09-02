class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        cur_area = 0
        max_area = 0


        while l < r:
            lowest_height = min(heights[l], heights[r])
            cur_area = (r - l) * lowest_height
            max_area = max(max_area, cur_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
