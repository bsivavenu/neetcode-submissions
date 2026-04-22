class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return True
        # if len(nums) > 1:
        #     for i in range(len(nums)-1):
        #         if nums[i]%2 == nums[i+1]%2:
        #             return False
        #         # else:
        #     return True

        return all(nums[i] % 2 != nums[i+1] % 2 for i in range(len(nums)-1))