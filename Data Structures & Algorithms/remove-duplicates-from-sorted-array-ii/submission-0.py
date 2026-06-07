class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array has 2 or fewer elements, it's already valid.
        if len(nums) <= 2:
            return len(nums)
        
        # 'k' points to the index where the next valid element should be placed.
        k = 2
        
        # Start iterating from the 3rd element (index 2)
        for i in range(2, len(nums)):
            # Check if the current element is different from the element 2 positions behind 'k'
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k