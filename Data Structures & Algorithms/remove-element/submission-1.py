class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        
        # nums[:]= [i for i in nums if i!= val]
        return len(nums)
