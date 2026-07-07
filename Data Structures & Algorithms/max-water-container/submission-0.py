class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        maximum_water = 0
        
        while l<r:
            height_left = heights[l]
            height_right = heights[r]
            
            area = min(height_left, height_right) * (r - l)
            
            maximum_water = max(maximum_water, area)

            if height_left < height_right:
                l +=1

            else:
                r -=1
        
        return maximum_water
