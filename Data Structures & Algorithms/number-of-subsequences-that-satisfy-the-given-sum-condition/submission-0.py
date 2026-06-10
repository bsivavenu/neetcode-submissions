class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        count = 0
        
        # Precompute powers of 2 to optimize performance
        # mapping index to 2^index % MOD
        pow2 = [1] * len(nums)
        for i in range(1, len(nums)):
            pow2[i] = (pow2[i - 1] * 2) % MOD
            
        while left <= right:
            if nums[left] + nums[right] <= target:
                # All subsequences anchored at 'left' up to 'right' are valid
                count = (count + pow2[right - left]) % MOD
                # Move the left pointer to check the next minimum element
                left += 1
            else:
                # The sum is too large, reduce the maximum element
                right -= 1
                
        return count