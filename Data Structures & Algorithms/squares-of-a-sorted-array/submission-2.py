class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted((i*i) for i in nums)
        n = len(nums)
        res = [0] * n  # Result array of the same size
        
        left = 0
        right = n - 1
        

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
                
        return res