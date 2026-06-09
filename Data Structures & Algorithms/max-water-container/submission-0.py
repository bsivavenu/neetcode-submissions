class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current width and height
            width = right - left
            current_height = min(heights[left], heights[right])
            
            # Calculate current area and update max_water if it's larger
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water