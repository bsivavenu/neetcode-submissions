class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x = {}
        # for i,j in enumerate(nums):
        #     y = target -j
        #     if y in x:
        #         return [x[y],i]
        #     x[j] = i

        

        sorted_nums = sorted((num,idx) for (idx,num) in enumerate(nums))
        # print(sorted_nums)

        left,right = 0, len(nums)-1

        while left < right:

            x = sorted_nums[left][0]+sorted_nums[right][0]
            if x  == target :
                return sorted([sorted_nums[left][1], sorted_nums[right][1]])
            elif x < target:
                left = left+1
            else:
                right = right-1
        