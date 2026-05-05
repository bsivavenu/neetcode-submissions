class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Assume both are true until proven otherwise
        increasing = True
        decreasing = True
        
        for i in range(len(nums) - 1):
            # If a later element is smaller, it's not monotone increasing
            if nums[i] > nums[i+1]:
                increasing = False
            # If a later element is larger, it's not monotone decreasing
            if nums[i] < nums[i+1]:
                decreasing = False
                
        # If it's still either one of them, the array is monotonic
        return increasing or decreasing