class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        area = 0
        maxA = 0
        cur_height = 0

        while l < r:
            cur_height = min(heights[l], heights[r])
            area = (r - l) * cur_height
            maxA = max(maxA, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxA

