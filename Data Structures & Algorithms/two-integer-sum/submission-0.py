class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+ nums[j] == target:
        #             return [i,j]
        x = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in x:
                return [x[diff],i]
            x[nums[i]] = i
