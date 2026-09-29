class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        l_max = height[0]
        r_max = height[-1]

        water = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                if height[l] < min(l_max, r_max):
                    water += min(l_max, r_max) - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                if height[r] < min(l_max, r_max):
                    water += min(l_max, r_max) - height[r]
        
        return water


