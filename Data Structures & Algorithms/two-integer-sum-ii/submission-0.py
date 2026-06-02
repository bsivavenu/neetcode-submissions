class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum