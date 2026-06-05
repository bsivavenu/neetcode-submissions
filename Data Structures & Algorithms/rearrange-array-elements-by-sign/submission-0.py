class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Initialize the result array with zeros of the same length
        ans = [0] * len(nums)
        
        # Pointers for the next available positive and negative slots
        pos_idx = 0
        neg_idx = 1
        
        # Traverse the original array
        for num in nums:
            if num > 0:
                ans[pos_idx] = num
                pos_idx += 2  # Move to the next even index
            else:
                ans[neg_idx] = num
                neg_idx += 2  # Move to the next odd index
                
        return ans