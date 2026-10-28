class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #it should hold the indexes
        max_area = 0

        for i, height in enumerate(heights + [0]):
            #check if the new height is smaller than top of stack for update
            while stack and heights[stack[-1]] > height:
                #now calculate the area
                height_idx = stack.pop()
                left = stack[-1] if stack else -1
                cur_height = heights[height_idx]

                cur_area = cur_height * (i - left - 1)
                max_area = max(max_area, cur_area)

            stack.append(i)

        return max_area


            #otherwise add it to the stack