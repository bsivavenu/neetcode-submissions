class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i= 0
        j = len(nums)-1
        while i < j:
            if nums[i] %2 == 0:
                i = i+1
            else :
                # nums[i]%2 > nums[j]%2 :
                nums[i], nums[j] = nums[j], nums[i]
                j = j-1
            
            # if nums[i] %2 == 0:
            #     i +=1
        return nums
