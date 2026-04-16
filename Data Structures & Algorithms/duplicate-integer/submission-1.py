class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if nums == list(set(nums)): 
        #     print('they are unique')
        #     return False
        # else: 
        #     return True

        return len(nums) != len(set(nums))