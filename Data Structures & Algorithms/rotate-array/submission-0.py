class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k is greater than the array length
        
        # Helper function to reverse a portion of the array in-place
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 1. Reverse the entire array
        reverse(0, n - 1)
        # 2. Reverse the first k elements
        reverse(0, k - 1)
        # 3. Reverse the rest of the elements
        reverse(k, n - 1)