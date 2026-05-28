class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_pointer = 0
        
        # Iterate through the array
        for current in range(len(nums)):
            # If the current element is non-zero, swap it
            if nums[current] != 0:
                nums[last_non_zero_pointer], nums[current] = nums[current], nums[last_non_zero_pointer]
                last_non_zero_pointer += 1